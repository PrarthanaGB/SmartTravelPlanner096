# 🌍 Smart Travel Planner

A full-stack web application that generates personalized travel itineraries with beautiful maps and recommendations. Users can register, log in, and input their destination, trip duration, budget, and preferred transportation mode to receive curated travel recommendations.

---

## ✨ Features

### 🔐 **User Authentication**

- User registration with email validation
- Secure login with password hashing (werkzeug.security)
- Session persistence using localStorage
- Profile welcome message with user email

### 🗺️ **Itinerary & Map Features**

- Generate customized travel recommendations
- Interactive Leaflet.js map with markers for:
  - 🏨 Hotels & Accommodations
  - 🍽️ Restaurants & Food Options
  - 🏥 Medical Facilities
  - 🚌 Transportation Hubs
  - 🎯 Tourist Attractions
- Category-based tabs for easy filtering
- Download itinerary as PDF

### 📍 **Supported Destinations**

- 🇮🇳 **Bengaluru** - Bangalore's tech hub with detailed attractions
- 🇮🇳 **Delhi** - India's capital with historic sites
- *(More cities coming in v1.1)*

### 💡 **Smart Recommendations**

- Day-by-day activity suggestions
- Budget-conscious recommendations
- Transportation mode preferences
- Location-based point of interest clustering

---

## 🏗️ Project Structure

```
SmartTravelPlanner/
├── backend/                      # Flask backend server
│   ├── app.py                   # Main Flask application
│   ├── config.py                # Configuration management
│   ├── database.py              # Database initialization
│   ├── requirements.txt          # Python dependencies
│   ├── configure.env             # Environment variables
│   ├── travel_db/               # Database files
│   ├── models/
│   │   └── user_model.py        # User database model
│   ├── routes/
│   │   ├── user_routes.py       # Authentication endpoints
│   │   └── ai_routes.py         # AI itinerary endpoints
│   └── utils/
│       └── ai_helper.py         # AI logic and utilities
│
├── frontend/                     # Frontend application
│   ├── index.html               # Main HTML structure
│   ├── css/
│   │   └── style.css            # Styling and layout
│   ├── js/
│   │   └── script.js            # Frontend logic
│   └── images/                  # Static assets
│
└── .venv/                        # Python virtual environment
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed
- **MySQL** database (or SQLite as fallback)
- **Node.js** (optional, for frontend enhancements)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd SmartTravelPlanner
   ```

2. **Set up Python environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install backend dependencies**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Update `configure.env` with your database credentials:

   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DB=travel_db
   SECRET_KEY=your_secret_key
   ```

5. **Run the application**
   ```bash
   cd backend
   python app.py
   ```
   The application will start on `http://localhost:5000`

---

## 🔧 Technology Stack

### Backend

- **Framework**: Flask 2.3.2
- **Database**: MySQL 8.0.33
- **Authentication**: Flask-CORS
- **Environment Management**: python-dotenv

### Frontend

- **HTML5** - Semantic markup
- **CSS3** - Modern responsive styling
- **JavaScript** - Dynamic interactivity
- **Leaflet.js** - Interactive mapping
- **RESTful API** - Communication with backend

---

## 📡 API Endpoints

### Authentication Routes

| Method | Endpoint    | Description               |
| ------ | ----------- | ------------------------- |
| POST   | `/register` | Create a new user account |
| POST   | `/login`    | User login with credentials |

### AI Routes

| Method | Endpoint | Description                   |
| ------ | -------- | ----------------------------- |
| POST   | `/ai`    | Generate itinerary recommendations |

**Example Request:**

```json
{
  "place": "Bengaluru",
  "days": 5,
  "budget": 2000,
  "transport": "flight"
}
```

**Supported Destinations (v1.0):**
- 🇮🇳 **Bengaluru** - India's Tech Hub
- 🇮🇳 **Delhi** - India's Capital
- ⚠️ Note: Other cities require database expansion (Coming Soon)

---

## 📝 Usage

1. **Register or Login**
   - Open `http://localhost:5000` in your browser
   - Create a new account or log in with existing credentials

2. **Plan Your Trip**
   - Navigate to the dashboard after login
   - Enter your travel details:
     - Destination
     - Number of days
     - Budget
     - Preferred transportation
   - Click "Generate Itinerary"

3. **View Recommendations**
   - Receive personalized itinerary with:
     - Day-by-day suggested activities
     - Popular attractions and restaurants
     - Hotels and medical facilities
     - Transport options
     - Points of interest displayed on interactive Leaflet map
   - Download itinerary as PDF
   - View route map with different categories (Stay, Food, Medical, Transport)

---

## 🗄️ Database Schema

### Users Table

- `id` - Primary key (AUTO_INCREMENT)
- `email` - User email (UNIQUE)
- `password` - Hashed password using werkzeug.security
- `created_at` - Account creation timestamp (Default: CURRENT_TIMESTAMP)

**Current Implementation:**
- User authentication and registration only
- Itineraries stored in frontend localStorage (not in database yet)
- Ready for future database expansion

---

## 🔒 Security Features

- ✅ Password hashing and secure storage
- ✅ CORS protection
- ✅ Environment variable management for sensitive data
- ✅ Session-based authentication
- ✅ SQL injection prevention through parameterized queries

---

## 📱 Responsive Design

The application is fully responsive and works seamlessly on:

- 💻 Desktop browsers
- 📱 Tablets
- 📲 Mobile devices

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💡 Future Enhancements (Roadmap)

### Phase 1 (v1.1)
- [ ] Add 5+ more Indian cities (Mumbai, Goa, Jaipur, etc.)
- [ ] Itinerary persistence to database
- [ ] User itinerary history and favorites

### Phase 2 (v1.2)
- [ ] Real AI integration (OpenAI API or similar)
- [ ] Real-time flight price tracking
- [ ] Hotel booking integration
- [ ] Multi-language support (Hindi, Spanish, etc.)

### Phase 3 (v2.0)
- [ ] Social sharing of itineraries
- [ ] User reviews and ratings for destinations
- [ ] Payment integration for bookings
- [ ] Advanced filtering and personalization
- [ ] Mobile app (React Native)
- [ ] Offline itinerary access with PWA

---

## 🐛 Troubleshooting

### Database Connection Issues

- The app will run in **demo mode** if MySQL is unavailable (user data won't persist)
- To use persistent storage:
  - Ensure MySQL is running: `services.msc` (Windows) or `brew services start mysql` (macOS)
  - Verify credentials in `backend/configure.env`
  - Create database: `CREATE DATABASE travel_db;`

### Flask Port Already in Use

Port 5000 is already in use? Kill the process:

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

Or change port in `backend/app.py`:
```python
app.run(debug=True, port=5001)  # Change to different port
```

### Frontend Not Loading

- Clear browser cache: **Ctrl+Shift+Delete** (Chrome/Edge)
- Verify Flask server is running: Visit `http://localhost:5000` in browser
- Check console for API errors: **F12** → Console tab
- Ensure static folder path is correct in `backend/app.py`

### Database in Demo Mode

- User registration works but won't persist after server restart
- To enable persistence, configure MySQL properly (see Database Connection Issues)

---

## 📞 Support

For issues and questions:

- Open an issue on GitHub
- Contact: [your-email@example.com]
- Check existing issues for solutions

---

## 🌟 Acknowledgments

- Flask community for an excellent web framework
- Leaflet.js for mapping capabilities
- MySQL for robust database management

---

**Happy Travel Planning! ✈️🗺️**
