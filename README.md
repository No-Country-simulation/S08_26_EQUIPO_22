<div align="center">

<img src="./industrial_ai_banner.png" width="100%">

<br>

# MaintAI Copilot

## Intelligent Predictive Maintenance Assistant

### Machine Learning and Local LLM for Industrial Equipment Diagnosis

<br>

<p>
MaintAI Copilot is an industrial predictive maintenance assistant that combines
Machine Learning, sensor data analysis and a local Large Language Model to
identify abnormal equipment conditions, interpret model results and provide
technical maintenance recommendations.
</p>

<br>

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge">

<img src="https://img.shields.io/badge/LLM-Ollama%20%2B%20Phi--3-4B8BBE?style=for-the-badge">

<img src="https://img.shields.io/badge/LangChain-AI%20Integration-1C3C3C?style=for-the-badge">

<img src="https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-FF4B4B?style=for-the-badge">

<img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge">

</div>


---

# Overview

MaintAI Copilot is a predictive maintenance application designed to support
industrial decision-making through Machine Learning, operational data
analysis and generative AI.

The system receives operational variables from industrial equipment, evaluates
their condition using a Machine Learning model and generates a technical
diagnosis that can be interpreted through a local LLM assistant.

The main purpose of the project is to transform equipment measurements into
information that can support maintenance and operational decisions.

---

# Industrial Challenge

Industrial equipment generates operational data related to vibration,
temperature, load, efficiency, electrical conditions and other operating
variables.

Traditional maintenance processes may rely heavily on periodic inspections
and manual interpretation of measurements. This can make it difficult to
identify abnormal conditions early and increase the risk of unexpected
downtime.

MaintAI Copilot approaches this problem through predictive analysis and
technical interpretation.

| Traditional Maintenance | MaintAI Approach |
|---|---|
| Reactive intervention after failures | Predictive equipment monitoring |
| Manual interpretation of measurements | Automated analysis of operational variables |
| Limited early-warning capability | Anomaly detection through Machine Learning |
| Isolated sensor information | Combined analysis of multiple variables |
| Manual technical interpretation | AI-assisted diagnosis |

---

# Solution Architecture

The general workflow of MaintAI Copilot is:

```text
Industrial Equipment Sensors
            |
            v
Operational Data
            |
            v
Data Processing
            |
            v
Machine Learning Model
            |
            v
Anomaly Detection
            |
            v
Technical Diagnosis
            |
            v
MaintAI Copilot
       LLM + Ollama
            |
            v
Maintenance Recommendations
