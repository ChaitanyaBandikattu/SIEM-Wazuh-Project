# 🚨 SIEM System using Wazuh for Real-Time Security Monitoring

> 🚀 A hands-on SIEM project simulating real-world SOC operations using Wazuh.

---

## 📌 Project Overview
This project demonstrates the design and implementation of a **Security Information and Event Management (SIEM)** system using Wazuh to monitor, analyze, and detect security events in real time within a simulated business environment.

The system aggregates logs from multiple sources such as servers and endpoints, performs event correlation, and generates alerts for suspicious activities like unauthorized access and brute-force attacks.

---

## ⚙️ Key Features
- Centralized log collection from servers and endpoints  
- Real-time monitoring and alert generation  
- Event correlation using predefined security rules  
- Detection of brute-force attacks and suspicious login attempts  
- Interactive dashboard visualization using ELK Stack  
- Log storage for forensic analysis and reporting  

---

## 🧠 Core Modules
- Log Collection & Processing  
- Event Correlation Engine  
- Alert Generation System  
- Monitoring Dashboard  
- Reporting & Database Integration  

---

## 🛠️ Technologies Used
- **Wazuh (SIEM Platform)**  
- **ELK Stack** – Elasticsearch, Logstash, Kibana  
- **Python (Flask)**  
- **Linux Environment**  

---

## 📸 Project Screenshots

### ⚙️ Implementation

### 📊 Results

---

## 🔄 Project Execution Workflow
1. Start Wazuh services on the SIEM server  
2. Start Wazuh agent on the client machine  
3. Run the Flask web application  
4. Perform attack simulations (failed login / sudo misuse)  
5. Monitor logs and alerts in the Wazuh dashboard  

---

## 🚨 Attack Simulation Scenarios
The system was tested using the following scenarios:

- Multiple failed login attempts (brute-force simulation)  
- Unauthorized sudo access attempts  

These activities generate logs that are captured, correlated, and analyzed by the SIEM system.

---

## 📊 Results
- Real-time alerts generated successfully  
- Detection of suspicious login activities  
- Logs visible in Wazuh Security Events dashboard  
- Effective identification of abnormal system behavior  

---

## ⚙️ Setup & Execution
For complete setup instructions and commands, refer to:  
📂 `setup/commands.txt`

---

## 🚀 Future Enhancements
- Automated incident response (e.g., IP blocking, account isolation)  
- Integration with threat intelligence feeds  
- Advanced analytics and visualization dashboards  
- Scalability improvements for enterprise environments  

---

## 💡 Conclusion
This project simulates real-world **Security Operations Center (SOC)** workflows by generating and analyzing security events using Wazuh. It provides hands-on experience in log monitoring, threat detection, and incident analysis.

---

## 👨‍💻 Author
**B. Chaitanya**  
Cybersecurity Student | SOC Analyst Aspirant  

🔗 GitHub: https://github.com/ChaitanyaBandikattu  
🔗 LinkedIn: https://www.linkedin.com/in/chaitanyabandikattu
