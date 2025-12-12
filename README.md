# Forecasting Tourism Demand in Singapore

A data-driven project leveraging historical tourism data, weather patterns, and major events to predict tourism demand in Singapore. Features regression analysis, forecasting models, and interactive visualizations to provide actionable insights for stakeholders in the tourism industry.

➡️ **[Live Demo of the Interactive Dashboard](#)** *(Replace with your link)*

---

### 1. The Business Problem

Tourism is a pillar of Singapore's economy, yet it is highly susceptible to external factors like seasonal fluctuations, weather conditions, and major events. For stakeholders such as hoteliers, tour operators, and government agencies, the inability to accurately forecast demand leads to significant operational inefficiencies.

* **Businesses** face revenue losses due to under-staffing during peak times or over-stocking during lulls.
* **Strategic Planners** lack visibility into how specific variables (e.g., the F1 Grand Prix or monsoon season) quantitatively impact visitor numbers.

This project tackles this uncertainty by moving from reactive observation to **proactive demand forecasting**, enabling stakeholders to optimize resources and maximize revenue based on data-backed predictions.

---

### 2. My Technical Approach

To achieve accurate forecasts, I developed a comprehensive data science pipeline using **Python**:

* **Data Collection & Integration:** Consolidated historical tourism statistics, meteorological data (rainfall, temperature), and calendars of major events using `Pandas` and `NumPy`.
* **Interactive EDA:** Leveraged `Plotly` (Express, Subplots, Graph Objects) and `Seaborn` to create dynamic charts that distinguish between regular seasonal trends and event-driven spikes.
* **Feature Engineering:** Used `StandardScaler` to normalize data and ensure model stability across different variable scales.
* **Model Training:** Developed a diverse set of predictive models to capture different data patterns:
    * **Linear Baselines:** `LinearRegression` and `LassoCV` to establish baseline trends.
    * **Machine Learning:** `RandomForestRegressor` and `XGBRegressor` (XGBoost) to capture complex, non-linear relationships between weather, events, and demand.
    * **Forecasting:** Implemented `Prophet` to handle seasonality and trend components specifically for time-dependent data.
* **Optimization & Evaluation:** Utilized `RandomizedSearchCV` for hyperparameter tuning and validated results using `mean_squared_error` (RMSE) and `r2_score`.

---

### 3. The Solution & Key Findings

The final solution provides a holistic view of the tourism landscape:

#### 🧭 **Data Analysis & Visualization**
* **Seasonal Trends:** Identified clear cyclical patterns, pinpointing peak travel windows (e.g., December holidays, Chinese New Year) using interactive Plotly charts.
* **Event Impact:** Quantified the surge in tourism activity during marquee events like the Formula 1 Grand Prix.
* **Weather Correlation:** Visualized the relationship between rainfall intensity and indoor vs. outdoor attraction demand.

#### 📊 **Prediction Model**
* **Forecasting Capability:** The `XGBoost` and `Prophet` models successfully predict future tourism demand with high reliability.
* **Evaluation:** The models achieved low RMSE scores, indicating precision in predicting visitor numbers against actual historical data.

**Key Findings:**
* **Resilience:** Major events serve as significant buffers against seasonal lows.
* **Weather Sensitivity:** While general tourism is resilient, specific outdoor activities show a strong negative correlation with heavy rainfall.

---

### 4. Business Impact

This project translates complex data into **strategic operational advantages**:

✅ **Resource Optimization**
Hotels and attractions can adjust staffing rosters and inventory procurement in advance, reducing wastage and overhead costs.

✅ **Dynamic Pricing Strategies**
Businesses can implement data-driven dynamic pricing models, capitalizing on predicted high-demand periods (e.g., event weekends).

✅ **Targeted Marketing**
Tourism boards can design marketing campaigns to boost arrivals during predicted low-demand seasons identified by the model.

---

### 5. Future Enhancements

* **Real-Time Data Streams:** Integrate live flight booking APIs or search engine trend data for "nowcasting" capabilities.
* **Sentiment Analysis:** Incorporate social media sentiment (Twitter/X, Instagram) to gauge global traveler interest in real-time.
* **Granular Forecasting:** Expand the model to predict demand by specific visitor demographics or accommodation types (luxury vs. budget).
* **Deep Learning:** Experiment with LSTM (Long Short-Term Memory) neural networks to better capture long-term dependencies.

---

### Author

**Kaung Si Thu**
[kaungsithu.sallius@gmail.com](mailto:kaungsithu.sallius@gmail.com)
