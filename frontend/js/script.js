let map;
let currentRouteData = null;
let currentTab = 'stay';
let routePolylines = [];

// Define marker colors and icons for different categories
const MARKER_CONFIG = {
    route: { color: '#0072ff', icon: '🎯' },
    stay: { color: '#FF6B6B', icon: '🏨' },
    food: { color: '#4ECDC4', icon: '🍽️' },
    medical: { color: '#FF69B4', icon: '🏥' },
    transport: { color: '#FFD93D', icon: '🚌' }
};

function getMarkerIcon(category) {
    const config = MARKER_CONFIG[category] || MARKER_CONFIG.route;
    return L.divIcon({
        html: `<div style="background-color: ${config.color}; color: white; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.3);">${config.icon}</div>`,
        iconSize: [40, 40],
        className: 'custom-marker'
    });
}

function updateAuthState() {
    const userEmail = localStorage.getItem('travelUser');
    const welcomeText = document.getElementById('welcomeText');
    if (userEmail) {
        welcomeText.textContent = `Welcome back, ${userEmail}!`;
        showDashboard();
    } else {
        showLogin();
    }
}

function showDashboard() {
    hideAllSections();
    document.getElementById('dashboard').classList.add('active');
}

function hideAllSections() {
    document.getElementById('login').classList.remove('active');
    document.getElementById('register').classList.remove('active');
    document.getElementById('dashboard').classList.remove('active');
    document.getElementById('route').classList.remove('active');
}

function initMap(coords, placeName, routePoints = [], extraPoints = [], categoryTab = 'stay') {
    if (map) {
        map.remove();
    }

    map = L.map('map').setView(coords, 12);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(map);

    const allMarkers = [];
    
    // Add route attraction markers with blue color
    if (routePoints.length > 0) {
        routePoints.forEach((point, idx) => {
            const marker = L.marker([point.lat, point.lng], {
                icon: getMarkerIcon('route')
            }).addTo(map);
            
            const popupContent = `<strong style="color: #0072ff;">${point.label}</strong><br/><span style="font-size: 12px;">Route Stop ${idx + 1}</span>`;
            marker.bindPopup(popupContent);
            allMarkers.push([point.lat, point.lng]);
        });

        // Draw polyline connecting route points
        if (routePoints.length > 1) {
            const routeLine = L.polyline(routePoints.map(p => [p.lat, p.lng]), {
                color: '#0072ff',
                weight: 3,
                opacity: 0.7,
                dashArray: '5, 5'
            }).addTo(map);
            routePolylines.push(routeLine);
        }
    }

    // Add nearby category markers
    if (extraPoints.length > 0) {
        extraPoints.forEach((point) => {
            const marker = L.marker([point.lat, point.lng], {
                icon: getMarkerIcon(categoryTab)
            }).addTo(map);
            
            const popupContent = `<strong style="color: ${MARKER_CONFIG[categoryTab].color};">${point.label}</strong>`;
            marker.bindPopup(popupContent);
            allMarkers.push([point.lat, point.lng]);
        });

        // Draw lines from city center to each nearby point
        if (routePoints.length > 0) {
            extraPoints.forEach(point => {
                const connectionLine = L.polyline([[coords[0], coords[1]], [point.lat, point.lng]], {
                    color: MARKER_CONFIG[categoryTab].color,
                    weight: 2,
                    opacity: 0.5,
                    dashArray: '2, 4'
                }).addTo(map);
                routePolylines.push(connectionLine);
            });
        }
    }

    // Add center marker for the city
    const centerMarker = L.circle(coords, {
        color: '#666',
        fillColor: '#999',
        fillOpacity: 0.5,
        radius: 500,
        weight: 2
    }).addTo(map);
    allMarkers.push(coords);

    // Fit map bounds to show all markers
    if (allMarkers.length > 0) {
        const group = new L.featureGroup(allMarkers.map(coords => L.marker(coords)));
        map.fitBounds(group.getBounds().pad(0.1));
    } else {
        map.setView(coords, 12);
    }
}

function showRoute() {
    if (!currentRouteData) {
        alert('Generate an itinerary first to view the route map.');
        return;
    }

    hideAllSections();
    document.getElementById('route').classList.add('active');
    currentTab = 'stay';
    setActiveTabButton(currentTab);
    initMap(currentRouteData.coords, currentRouteData.place, currentRouteData.route_points, (currentRouteData.nearby && currentRouteData.nearby.stay) || [], 'stay');
    renderRouteDetails(currentRouteData, currentTab);
}

function backToDashboard() {
    showDashboard();
    // Clear polylines when leaving map
    routePolylines.forEach(line => line.remove());
    routePolylines = [];
}

function showRegister() {
    hideAllSections();
    document.getElementById('register').classList.add('active');
}

function showLogin() {
    hideAllSections();
    document.getElementById('login').classList.add('active');
}

function logout() {
    localStorage.removeItem('travelUser');
    currentRouteData = null;
    hideAllSections();
    showLogin();
}

function setActiveTabButton(tabName) {
    ['stay', 'food', 'medical', 'transport'].forEach(name => {
        const button = document.getElementById(`tab-${name}`);
        if (button) {
            button.classList.toggle('active', name === tabName);
        }
    });
}

function showTab(tabName) {
    if (!currentRouteData) {
        alert('Generate an itinerary first before viewing nearby options.');
        return;
    }
    currentTab = tabName;
    setActiveTabButton(tabName);
    // Clear previous polylines
    routePolylines.forEach(line => line.remove());
    routePolylines = [];
    // Initialize map with new category
    initMap(currentRouteData.coords, currentRouteData.place, currentRouteData.route_points, (currentRouteData.nearby && currentRouteData.nearby[tabName]) || [], tabName);
    renderRouteDetails(currentRouteData, tabName);
}

function renderRouteDetails(data, activeTab = 'stay') {
    const routeDetails = document.getElementById('route-details');
    const routeItems = data.route_points.map(point => `<li>${point.label}</li>`).join('');
    const categoryPoints = (data.nearby && data.nearby[activeTab]) || [];

    routeDetails.innerHTML = `
        <div class="route-summary-card">
            <h3>${data.place} Route Summary</h3>
            <p><strong>Current view:</strong> ${activeTab.charAt(0).toUpperCase() + activeTab.slice(1)}</p>
            <p><strong>Hotel suggestion:</strong> ${data.hotel}</p>
            <p><strong>Transport style:</strong> ${data.transport}</p>
            <p><strong>Route stops:</strong></p>
            <ul>${routeItems}</ul>
            <p><strong>${categoryPoints.length} nearby ${activeTab} options found</strong></p>
        </div>
    `;
    renderTabContent(activeTab, categoryPoints);
}

function renderTabContent(tabName, points = []) {
    const categoryContent = document.getElementById('route-category-content');
    if (!categoryContent) return;

    const titleMap = {
        'stay': 'Stay Options',
        'food': 'Food & Dining',
        'medical': 'Medical Facilities',
        'transport': 'Transport Hubs'
    };
    
    const descriptionMap = {
        'stay': 'Recommended hotels and comfortable stays near your route.',
        'food': 'Popular local food spots and dining choices near the itinerary.',
        'medical': 'Nearby medical facilities and hospitals for safe travel support.',
        'transport': 'Airport, railway stations, and bus terminals for easy connectivity.'
    };

    const title = titleMap[tabName] || 'Nearby Services';
    const description = descriptionMap[tabName] || 'Nearby services available for your trip.';

    const listItems = points.length > 0
        ? points.map(point => `<li>${point.label}</li>`).join('')
        : `<li>No nearby options found yet. Try generating a new itinerary.</li>`;

    categoryContent.innerHTML = `
        <h3>${title}</h3>
        <p>${description}</p>
        <ul>${listItems}</ul>
    `;
}

function login(event) {
    event.preventDefault();

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;

    if (!email || !password) {
        alert('Please enter both email and password.');
        return;
    }

    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    })
    .then(response => response.json().then(body => ({ status: response.status, body })))
    .then(result => {
        if (result.status === 200) {
            localStorage.setItem('travelUser', email);
            updateAuthState();
        } else {
            alert(result.body.message || 'Login failed.');
        }
    })
    .catch(error => {
        console.error('Login error:', error);
        alert('Unable to connect to the backend. Make sure the server is running.');
    });
}

function register(event) {
    event.preventDefault();

    const email = document.getElementById('reg-email').value.trim();
    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('reg-confirm-password').value;

    if (!email || !password || !confirmPassword) {
        alert('Please fill in all registration fields.');
        return;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    })
    .then(response => response.json().then(body => ({ status: response.status, body })))
    .then(result => {
        if (result.status === 200 || result.status === 201) {
            alert(result.body.message || 'Registration successful! Please log in.');
            showLogin();
        } else {
            alert(result.body.message || 'Registration failed.');
        }
    })
    .catch(error => {
        console.error('Registration error:', error);
        alert('Unable to register. Make sure the backend is running.');
    });
}

function showItinerary(data) {
    const plansContainer = document.getElementById('plans');
    plansContainer.innerHTML = '';

    const summary = document.createElement('div');
    summary.className = 'itinerary-summary';
    summary.innerHTML = `
        <h3>${data.place} - ${data.days}-Day Trip</h3>
        <p><strong>Budget:</strong> ${data.budget} total</p>
        <p><strong>Daily budget:</strong> ${data.daily_budget}</p>
        <p><strong>Transport style:</strong> ${data.transport}</p>
        <p><strong>Hotel suggestion:</strong> ${data.hotel}</p>
        <p>${data.plans[0].summary}</p>
    `;
    plansContainer.appendChild(summary);

    const routeSummary = document.createElement('div');
    routeSummary.className = 'route-summary';
    routeSummary.innerHTML = `
        <h4>Route Overview</h4>
        <p>Planned points: ${data.route_points.length}</p>
    `;
    plansContainer.appendChild(routeSummary);

    data.plans.forEach((plan, index) => {
        const planCard = document.createElement('div');
        planCard.className = 'plan-card';
        planCard.innerHTML = `<h3>${plan.name}</h3><p>${plan.summary}</p>`;

        plan.details.forEach(dayPlan => {
            const daySection = document.createElement('div');
            daySection.className = 'day-plan';
            daySection.innerHTML = `
                <h4>${dayPlan.day}: ${dayPlan.title}</h4>
                <p><strong>Transport:</strong> ${dayPlan.transport}</p>
                <p><strong>Recommended meal:</strong> ${dayPlan.recommended_meal}</p>
                <ul>${dayPlan.activities.map(item => `<li>${item}</li>`).join('')}</ul>
            `;
            planCard.appendChild(daySection);
        });

        plansContainer.appendChild(planCard);
    });

    const downloadButton = document.getElementById('downloadButton');
    if (downloadButton) {
        downloadButton.style.display = 'block';
    }
}

function downloadItinerary() {
    if (!currentRouteData) {
        alert('Please generate an itinerary first.');
        return;
    }

    const textLines = [];
    textLines.push(`Travel Planner Itinerary for ${currentRouteData.place}`);
    textLines.push(`Days: ${currentRouteData.days}`);
    textLines.push(`Budget: ${currentRouteData.budget}`);
    textLines.push(`Daily Budget: ${currentRouteData.daily_budget}`);
    textLines.push(`Transport: ${currentRouteData.transport}`);
    textLines.push(`Hotel suggestion: ${currentRouteData.hotel}`);
    textLines.push('');
    textLines.push('Route Points:');
    currentRouteData.route_points.forEach((point, index) => {
        textLines.push(`${index + 1}. ${point.label} (${point.lat.toFixed(5)}, ${point.lng.toFixed(5)})`);
    });
    textLines.push('');

    currentRouteData.plans.forEach(plan => {
        textLines.push(`Plan: ${plan.name}`);
        textLines.push(`${plan.summary}`);
        plan.details.forEach(dayPlan => {
            textLines.push(`\n${dayPlan.day} - ${dayPlan.title}`);
            textLines.push(`Transport: ${dayPlan.transport}`);
            textLines.push(`Recommended meal: ${dayPlan.recommended_meal}`);
            dayPlan.activities.forEach(activity => textLines.push(`- ${activity}`));
        });
        textLines.push('');
    });

    const blob = new Blob([textLines.join('\n')], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${currentRouteData.place}_itinerary.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}


function renderRouteDetails(data) {
    const routeDetails = document.getElementById('route-details');
    routeDetails.innerHTML = '';

    const pointsList = data.route_points.map(point => `<li>${point.label}</li>`).join('');
    routeDetails.innerHTML = `
        <div class="route-summary-card">
            <h3>Route Points</h3>
            <ul>${pointsList}</ul>
            <p><strong>Hotel:</strong> ${data.hotel}</p>
            <p><strong>Transport style:</strong> ${data.transport}</p>
        </div>
    `;
}

function askAI() {
    const place = document.getElementById('place').value.trim();
    const days = document.getElementById('days').value;
    const budget = document.getElementById('budget').value;
    const transport = document.getElementById('transport').value.trim();

    if (!place || !days || !budget || !transport) {
        alert('Please fill in all travel details.');
        return;
    }

    fetch('http://127.0.0.1:5000/ai', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ place, days, budget, transport })
    })
    .then(response => response.json())
    .then(data => {
        if (!data || !data.plans || data.plans.length === 0) {
            alert('No itinerary returned. Try another city or adjust your budget.');
            return;
        }
        currentRouteData = data;
        showItinerary(data);
    })
    .catch(error => {
        console.error('AI request error:', error);
        alert('Unable to fetch AI plans. Make sure the backend is running.');
    });
}

function showTab(tabName) {
    const chatbot = document.getElementById('chatbot');
    chatbot.textContent = `Showing ${tabName} options and nearby services for this travel plan.`;
}

window.addEventListener('DOMContentLoaded', () => {
    updateAuthState();
});
