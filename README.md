# Product Registration Automation 🤖

A Python automation script built with `PyAutoGUI` and `pandas` to automate filling and submitting the **Product Registration Project** web form using data from a `products.csv` file.

This repository automates the web interface hosted at `https://rafael211808.github.io/Register-Products-Project/` (corresponding to the **Register-Products-Project** repository)[cite: 6].

## 🚀 How It Works

- **CSV Data Loading:** Reads product entries (`code`, `brand`, `type`, `category`, `unit_price`, `cost`, and optional `note`) from `products.csv` using `pandas`[cite: 6].
- **Browser Automation:** Opens Google Chrome and navigates to the target Product Registration web application[cite: 6].
- **Form Filling & Submission:** Iterates through each row in the CSV, navigates fields via keyboard inputs (`tab` and `write`), submits the form, dismisses the confirmation dialog, and scrolls back up for the next record[cite: 6].

## 🛠️ Technologies Used

- **Python**
- **PyAutoGUI:** GUI and keyboard/mouse automation[cite: 6]
- **pandas:** CSV reading and tabular data iteration[cite: 6]

## 📂 Project Structure

```text
├── main.py         # Automation script
└── products.csv    # Product dataset used to populate the form
