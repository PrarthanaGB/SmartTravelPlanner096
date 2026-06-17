# 🌍 Smart Travel Planner

A full-stack web application that leverages AI to generate personalized travel itineraries. Users can input their destination, trip duration, budget, and preferred transportation mode to receive AI-powered travel recommendations.

---

## ✨ Features

### 🔐 **User Authentication**

- User registration and login functionality
- Secure password handling
- Session management with logout

### 🤖 **AI-Powered Itinerary Generation**

- Smart recommendations based on:
  - **Destination** - Select any place in the world
  - **Duration** - Trip length in days
  - **Budget** - Cost constraints for better recommendations
  - **Transportation** - Preferred travel mode (flight, train, car, etc.)

### 📍 **Interactive Dashboard**

- User-friendly interface for trip planning
- Real-time map integration (Leaflet.js)
- Quick and easy itinerary generation

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
| POST   | `/login`    | User login                |
| POST   | `/logout`   | User logout               |

### AI Routes

| Method | Endpoint | Description                   |
| ------ | -------- | ----------------------------- |
| POST   | `/ai`    | Generate AI-powered itinerary |

**Example Request:**

```json
{
  "place": "Paris",
  "days": 5,
  "budget": 2000,
  "transport": "flight"
}
```

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
   - Receive AI-generated itinerary with:
     - Day-by-day activities
     - Estimated costs
     - Transportation suggestions
     - Points of interest with map integration

---

## 🗄️ Database Schema

### Users Table

- `id` - Primary key
- `email` - User email
- `password` - Hashed password
- `created_at` - Account creation timestamp

### Itineraries Table

- `id` - Primary key
- `user_id` - Foreign key to users
- `destination` - Trip destination
- `duration` - Number of days
- `budget` - Trip budget
- `transportation` - Preferred mode
- `generated_plan` - AI-generated itinerary
- `created_at` - Generation timestamp

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

## 💡 Future Enhancements

- [ ] Multi-language support
- [ ] Real-time price tracking for flights and hotels
- [ ] User reviews and ratings for destinations
- [ ] Social sharing of itineraries
- [ ] Offline itinerary access
- [ ] Payment integration for bookings
- [ ] Advanced filtering and personalization

---

## 🐛 Troubleshooting

### Database Connection Issues

- Ensure MySQL is running
- Verify credentials in `configure.env`
- Check database exists: `travel_db`

### Flask Port Already in Use

```bash
# Find and kill process on port 5000
netstat -ano | findstr :5000  # Windows
lsof -i :5000  # macOS/Linux
```

### Frontend Not Loading

- Clear browser cache (Ctrl+Shift+Delete)
- Verify Flask server is running
- Check console for API errors (F12)

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
