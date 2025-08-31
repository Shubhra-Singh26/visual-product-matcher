Visual Product Matcher
This project is a web application that allows users to upload an image of a product and receive visually similar products from a predefined catalog. The matched products are displayed with their images, descriptions, categories, prices, and similarity percentages.

Features
Upload a product image via the web interface.

Preview the uploaded image before searching.

Backend processes the uploaded image and returns similar products.

Displays similar products with images and relevant details.

Responsive frontend with simple and clean UI.

Sample product catalog stored in products.json.

Serves static images and frontend files via Flask backend.

Project Structure
text
project-root/
│
├── backend/
│   ├── server.py             # Flask backend server
│   ├── products.json         # Product catalog JSON data
│   └── images/               # Folder with product images
│
├── frontend/
│   ├── index.html            # Frontend HTML file
│   ├── style.css             # CSS styles
│   └── app.js                # JavaScript logic (image upload, rendering)
Setup and Run
Prerequisites
Python 3.7+

Flask (pip install flask)

Web browser

Steps
Prepare images and catalog:

Place all product images in the backend images/ folder.

Make sure products.json references images correctly with /images/ prefix.

Run Flask backend:

bash
cd backend
python server.py
The backend runs on http://127.0.0.1:5000.

Access frontend:

Open browser and navigate to http://127.0.0.1:5000 (served by Flask).

Alternatively, you can open frontend/index.html directly, but for full functionality, serve frontend via Flask or a local web server.

Use the app:

Click "Choose File" to upload a product image.

View the preview and wait for matched results.

Similar products with descriptions will appear under "Results".

How It Works
Frontend sends the uploaded image as a POST request to the backend /match endpoint.

Backend loads the products.json catalog.

(Placeholder) Backend randomly selects similar products and adds a fake similarity score.

Backend responds with JSON data of matched products.

Frontend receives the JSON and dynamically renders product cards with images, names, category, price, and similarity score.

Notes and Future Improvements
Current matching logic is a placeholder and randomly returns products.

For a production system, integrate image feature extraction (e.g., with OpenCV, TensorFlow) and similarity search to find truly visually similar products.

Add error handling on frontend and backend.

Add better UI/UX (loading indicators, messages when no results found).

Optimize image sizes and caching for faster load times.

Testing Backend API
Use Postman or curl to test the /match API:

bash
curl -X POST -F image=@path/to/image.jpeg http://127.0.0.1:5000/match
The response should be a JSON array of similar products.
