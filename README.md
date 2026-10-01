<div align="center">

<img src="./industrial_ai_banner.png" width="100%">

<br>

# ⚙️ MaintAI Copilot

## Intelligent Predictive Maintenance Assistant

### Machine Learning + Local LLM for Industrial Equipment Diagnosis

<br>

<p>
MaintAI Copilot is an intelligent industrial maintenance assistant that combines
Machine Learning, sensor analytics and Large Language Models to detect abnormal
equipment conditions, explain predictive results and generate technical
maintenance recommendations.
</p>

<br>

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge">

<img src="https://img.shields.io/badge/LLM-Ollama%20%2B%20Phi--3-4B8BBE?style=for-the-badge">

<img src="https://img.shields.io/badge/LangChain-AI%20Integration-1C3C3C?style=for-the-badge">

<img src="https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-FF4B4B?style=for-the-badge">

<img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge">


<br><br>

</div>


# 🚀 Overview

MaintAI Copilot is a predictive maintenance platform designed to support
industrial decision-making by combining predictive analytics and generative AI.

The system analyzes operational variables from industrial equipment,
identifies abnormal conditions through Machine Learning models and provides
technical explanations through an AI maintenance assistant.

The objective is to transform raw sensor measurements into actionable
maintenance insights.


---

# 🏭 Industrial Challenge

Industrial equipment continuously generates large amounts of operational data:

<table>
<tr>

<td width="50%">

<h3>Traditional Approach</h3>

<ul>
<li>Reactive maintenance after failures</li>
<li>Manual interpretation of measurements</li>
<li>Limited early warning capability</li>
<li>High risk of unexpected downtime</li>
</ul>

</td>


<td width="50%">

<h3>AI-Based Approach</h3>

<ul>
<li>Predictive equipment monitoring</li>
<li>Automatic anomaly identification</li>
<li>Risk assessment</li>
<li>Technical AI assistance</li>
</ul>

</td>

</tr>
</table>


---

# 🧠 MaintAI Solution Architecture


```
Industrial Equipment Sensors

            │

            ▼

Operational Data Processing

            │

            ▼

Machine Learning Prediction Model

            │

            ▼

Equipment Condition Diagnosis

            │

            ▼

MaintAI Copilot

(LLM + LangChain + Ollama)

            │

            ▼

Technical Maintenance Recommendations
```


---

# ⚙️ Main Capabilities


<table>

<tr>

<td width="33%" align="center">

<h3>📊 Predictive Analytics</h3>

<p>
Machine Learning models analyze equipment variables to identify abnormal
operating conditions.
</p>

</td>


<td width="33%" align="center">

<h3>📈 Industrial Dashboard</h3>

<p>
Interactive visualization of KPIs, risk levels, trends and critical factors.
</p>

</td>


<td width="33%" align="center">

<h3>🤖 AI Copilot</h3>

<p>
A local LLM assistant explains diagnosis results and supports maintenance teams.
</p>

</td>


</tr>

</table>


---

# 🔍 Diagnostic Variables


The predictive system analyzes industrial indicators including:


| Category | Variables |
|---|---|
| Vibration | RMS vibration, peak vibration, kurtosis, crest factor |
| Thermal | Bearing temperature, motor temperature, thermal gradients |
| Electrical | Current imbalance, power factor, active power |
| Mechanical | Load conditions, operating speed |
| Efficiency | Operational efficiency indicators |


---

# 🤖 MaintAI Copilot

The integrated AI assistant provides technical interpretation of Machine
Learning outputs.

Capabilities:

✔ Equipment condition explanation  
✔ Risk interpretation  
✔ Critical variable identification  
✔ Possible technical causes  
✔ Maintenance recommendations  


Example interaction:

```
User:
Analyze the current condition of equipment MGG001.


MaintAI:

1. Equipment condition
2. Risk level
3. Critical variables
4. Possible causes
5. Recommended maintenance action
```


---

# 🏗️ System Architecture


```
                 MaintAI Copilot


        ┌─────────────────────┐
        │  Streamlit Interface │
        └──────────┬──────────┘
                   │

        ┌──────────▼──────────┐
        │ Dashboard Components │
        └──────────┬──────────┘
                   │

        ┌──────────▼──────────┐
        │ ML Prediction Engine │
        └──────────┬──────────┘
                   │

        ┌──────────▼──────────┐
        │ LLM Technical Layer  │
        │ Ollama + Phi-3 Mini  │
        └─────────────────────┘

```


---

# 📂 Project Structure


```
MaintAI-Copilot/

│
├── app.py
│
├── components/
│   ├── dashboard.py
│   ├── chat.py
│   ├── charts.py
│   ├── filters.py
│   ├── kpis.py
│   └── styles.py
│
├── src/
│   ├── pipeline.py
│   ├── llm_connector.py
│   └── knowledge_base.py
│
├── models/
│   └── Machine Learning Models
│
├── data/
│   └── Industrial Data
│
├── assets/
│   └── Interface Resources
│
└── requirements.txt

```


---

# 🛠️ Technology Stack


<table>

<tr>
<th>Layer</th>
<th>Technology</th>
</tr>


<tr>
<td>Programming</td>
<td>Python 3.11</td>
</tr>


<tr>
<td>Machine Learning</td>
<td>Scikit-Learn</td>
</tr>


<tr>
<td>AI Framework</td>
<td>LangChain</td>
</tr>


<tr>
<td>Local LLM Runtime</td>
<td>Ollama</td>
</tr>


<tr>
<td>Language Model</td>
<td>Phi-3 Mini</td>
</tr>


<tr>
<td>User Interface</td>
<td>Streamlit</td>
</tr>


<tr>
<td>Visualization</td>
<td>Plotly</td>
</tr>


</table>


---

# 📊 Predictive Maintenance Workflow


```
Data Acquisition

        ↓

Feature Processing

        ↓

Machine Learning Model

        ↓

Risk Evaluation

        ↓

AI Interpretation

        ↓

Maintenance Decision Support

```


---

# 🎯 Project Objective


Develop an intelligent industrial assistant capable of combining predictive
analytics and generative artificial intelligence to support maintenance teams
in identifying equipment conditions before failures occur.


---

# 👨‍💻 Development Team


<div align="center">

## S08_26_EQUIPO_22

Industrial AI Predictive Maintenance Project

</div>


---

# ⭐ Future Improvements


- Real-time sensor integration
- Historical equipment monitoring
- RAG-based technical knowledge system
- Automated maintenance alerts
- Cloud deployment
- MLOps pipeline integration

