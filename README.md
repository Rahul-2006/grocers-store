# Grocers-Store 🛒<br>
This is a full-stack grocery store web application built using Flask, MySQL, HTML, CSS, and JavaScript. It allows users to browse products, add items to their cart, and place orders seamlessly.

## ✨ Features<br>
- **🛍️ View products with pricing and unit details<br>**
- **🛒 Add items to the cart and manage quantity<br>**
- **✅ Place orders, storing them in the database<br>**
- **📊 Backend API with proper CORS handling for smooth frontend communication<br>**
- **🚀 Deployed using Render (backend) and Netlify (frontend)<br>**

## 📂 Files Overview<br>
### Backend (/backend)<br>
- `server.py` → Flask server handling requests and database operations<br>
- `sql_connector.py` → Connects to the MySQL database<br>
- `products_dao.py` → Handles product queries from the database<br>
- `orders_dao.py` → Manages order-related database transactions<br>
- `requirements.txt` → Dependencies for running Flask and MySQL connection<br>

### Frontend (/ui)<br>
- **`index.html`** → Landing page for the store<br>
- **`shop.html`** → Displays products and order functionality<br>
- **`script.js`** → Handles API requests and UI updates<br>

## ⚙️ Requirements<br>
- Python 3.x<br>
- Flask (pip install flask flask-cors)<br>
- MySQL Server (Railway-hosted)<br>
- `mysql-connector-python` (pip install mysql-connector-python)<br>
- Netlify (for frontend deployment)<br>

## 🚀 Deployment & Uptime Monitoring  
- **Backend:** Render → [https://grocers-store.onrender.com](https://grocers-store.onrender.com)  
- **Frontend:** Netlify → [https://grocerstore.netlify.app](https://grocerstore.netlify.app)  
- **Uptime Monitoring:** UptimeRobot pings the backend every 5 minutes to keep it active.    

## 🏁 How to Run Locally<br>
### Backend Setup<br>
1️⃣ Ensure MySQL is running with correct database schema<br>
2️⃣ Open terminal, navigate to backend folder (cd backend/)<br>
3️⃣ Install dependencies:<br>

```bash
pip install -r requirements.txt
```
<br>
4️⃣ Run Flask server:<br>

```bash
python server.py
```
<br>
5️⃣ Backend should be available at http://127.0.0.1:5000/<br>

### Frontend Setup<br>
1️⃣ Navigate to ui folder (cd ui/)<br>
2️⃣ Use a simple local server to preview:<br>

```bash
npx serve .  # OR python -m http.server
```
<br>
