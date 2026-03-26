# AgriTech-Yield-Risk-Predictor

🌾 **Precision Crop Yield & Risk Predictor with Digital Twin**

Agri-Tech is an AI-powered platform that predicts crop yield, assesses farming risks, and creates a Digital Twin of farmland for simulation and analysis. Using weather, soil, and crop data, it provides predictive insights and smart farming recommendations to support data-driven decisions and improve agricultural productivity and sustainability.

## 📌 Project Overview

Agri-Tech is an AI-driven decision support system designed to enhance agricultural productivity through crop yield forecasting, risk assessment, and Digital Twin-based farm simulation. The platform integrates weather parameters, soil characteristics, and historical crop data to generate predictive insights, risk alerts, and actionable recommendations via an interactive analytical dashboard.

## 🎯 Problem Statement

Modern agriculture faces multiple uncertainties that impact crop productivity, including:
- Climate variability and extreme weather conditions
- Soil degradation and nutrient imbalance
- Increased probability of crop failure
- Lack of predictive, data-driven farming tools

The proposed system addresses these challenges by delivering AI-powered yield prediction, agricultural risk modeling, and digital farm visualization to support informed decision-making.

## 🚀 Key Features

- 🌱 **Machine Learning–based Crop Yield Prediction** - Forecasts crop productivity using ensemble models
- ⚠️ **Agricultural Risk Assessment** - Identifies risks (drought, low productivity, pest issues, etc.)
- 🛰️ **Digital Twin–based Virtual Farm Visualization** - Simulates farm scenarios and outcomes
- 📊 **Interactive Data Dashboard** - Real-time analytics and performance metrics
- 💡 **Intelligent Farming Recommendations** - Actionable insights for optimized farming practices

## 🛠️ Technology Stack

- **Backend**: Python
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Data Processing**: CSV, Pandas DataFrames
- **Frontend**: HTML, CSS, JavaScript
- **Web Framework**: Flask
- **Visualization**: Matplotlib, Plotly
- **Version Control**: Git & GitHub
- **Model Storage**: Pickle (PKL files with Git LFS)

## 📂 Project Structure

```
AgriTech-Yield-Risk-Predictor/
│
├── app.py                          # Main Flask application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # Project license
│
├── backend/
│   ├── __init__.py
│   ├── data/
│   │   ├── raw/                   # Original datasets
│   │   │   ├── agriculture_dataset.csv
│   │   │   ├── Crop_Recommendation.csv
│   │   │   ├── ICRISAT-District Level Data.csv
│   │   │   ├── India Agriculture Crop Production.csv
│   │   │   └── [Other raw datasets]
│   │   └── processed/             # Cleaned & preprocessed data
│   │       ├── crop_recommendation_dataset.csv
│   │       └── yield_dataset.csv
│   │
│   ├── ml/                        # Machine Learning modules
│   │   ├── predictor.py           # Yield prediction model
│   │   ├── train_yield_model.py   # Model training script
│   │   └── train_recommendation_model.py
│   │
│   ├── logic/                     # Business logic & prediction endpoints
│   │   ├── predictor.py           # Prediction logic
│   │   └── recommender.py         # Recommendation engine
│   │
│   ├── preprocessing/             # Data preprocessing pipelines
│   │   ├── preprocess_yield.py
│   │   └── preprocess_recommendation.py
│   │
│   ├── digital_twin/              # Digital Twin simulation
│   │   ├── farm_simulation.py     # Farm scenario simulation
│   │   └── visualizations.py      # Simulation visualizations
│   │
│   └── models/                    # Trained ML models (stored with Git LFS)
│       ├── yield_model.pkl
│       └── recommendation_model.pkl
│
├── frontend/
│   ├── templates/
│   │   └── index.html             # Main UI page
│   └── static/
│       ├── css/
│       │   └── style.css          # Stylesheet
│       ├── js/
│       │   └── script.js          # Frontend logic
│       ├── images/                # UI images & icons
│       └── video/                 # Demo videos
│
├── tests/                         # Test suites
│   ├── test_yield_prediction.py
│   ├── test_risk_prediction.py
│   ├── test_input_validation.py
│   └── test_digital_twin.py
│
└── .gitattributes                 # Git LFS configuration for large files
```

## 💻 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git & Git LFS (for handling large model files)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/techievansh/AgriTech-Yield-Risk-Predictor.git
   cd AgriTech-Yield-Risk-Predictor
   ```

2. **Install Git LFS** (for large model files)
   ```bash
   git lfs install
   git lfs pull
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Application

### Start the Flask Server
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Running Tests
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python -m pytest tests/test_yield_prediction.py
python -m pytest tests/test_risk_prediction.py
python -m pytest tests/test_digital_twin.py
```

## 📊 Model Training

To retrain the ML models with updated data:

```bash
# Train yield prediction model
python backend/ml/train_yield_model.py

# Train crop recommendation model
python backend/ml/train_recommendation_model.py
```

## 🔄 Current Implementation Status

### ✅ Completed
- Data preprocessing pipelines for yield and recommendation datasets
- Machine learning models for crop yield prediction
- Risk assessment algorithms
- Digital Twin farm simulation engine
- Backend API endpoints for predictions
- Frontend dashboard with interactive UI
- Model persistence with PKL files (Git LFS enabled)

### 🔄 In Progress / Future Enhancements
- Advanced visualization dashboards (Plotly/Streamlit integration)
- Real-time weather API integration
- Mobile app support
- Cloud deployment (AWS/GCP)
- Explainable AI features
- Multi-language support

## 📝 Data Sources

The project uses agricultural datasets from:
- ICRISAT (International Crops Research Institute for the Semi-Arid Tropics)
- FAO (Food and Agriculture Organization)
- Government agricultural data repositories
- Indian agricultural production records

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vansh** - [GitHub Profile](https://github.com/techievansh)

## 📧 Contact & Support

For questions, suggestions, or issues, please open a GitHub issue or contact the development team.

---

**Note:** Large model files (yield_model.pkl, etc.) are stored using Git LFS. Ensure Git LFS is installed and initialized before cloning the repository.
