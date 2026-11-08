# Digital Movie Ticket Booking System 🎬🍿

A Python-based Digital Movie Ticket Booking simulator built from scratch using core **Object-Oriented Programming (OOP)** principles. This application models a real-world cinema booking experience, handling everything from managing show catalogs to dynamic seat grids and secure ticket dispatch.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Show Catalog Management:** Browse a dynamic list of currently screening movies along with their genres, durations, and available show timings.
*   **Interactive Seat Selection Layout:** Displays a simulated seat matrix allowing users to select rows and seat numbers in real-time.
*   **Booking Validation Matrix:** Automatically checks seat availability to completely prevent double-booking or overwriting of pre-booked seats.
*   **Tiered Pricing Tiers:** Supports differential pricing models based on seat category (e.g., Silver, Gold, Platinum/Recliner).
*   **Automated Ticket Generation:** Calculates overall balances, applies simulated convenience fees, and generates a structured digital invoice.

---

## 🛠️ OOP Concepts Implemented

This project focuses heavily on structured data design and clean component interaction:
*   **Classes & Objects:** Divided cleanly into logical modules with dedicated blueprints like `Movie`, `Show`, `CinemaHall`, and `Ticket`.
*   **Composition:** The `CinemaHall` and `Show` classes act as containers for `Movie` objects and multidimensional list matrices representing seats, establishing solid component relationships.
*   **Encapsulation:** Keeps transaction metrics and inner layout arrays secure from outside interference via private structural variables, updating status only through validated booking methods.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd digital-movie-ticket-booking
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.
