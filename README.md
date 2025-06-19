# 📚 Library Management System

A console-based Library Management System built with Python. This system allows users to
register, borrow, return, reserve, and search for library items like books, DVDs, and magazines.
Data is stored using JSON files.

Note: You can't reserve Magazine items .
---

## 🚀 Features

- 🔍 Search for items by title or type
- 📦 View available and borrowed items
- 🙋 Register new users
- 📥 Borrow items
- 🕒 Reserve items (queue system)
- 📤 Return borrowed items
- ❌ Remove users and items
- ✅ Custom exceptions for better error handling

---

👀 Additional Highlights
✅ Each item in the items.json file can include a reservation queue that tracks the order of users waiting to borrow it.

🏛️ All core logic — including reading/writing JSON and business rules — is implemented inside the Library class.

🕒 The reserve function allows users to reserve items that are currently borrowed. Once the item is returned, the first user in the reservation queue gets priority to borrow it.

🎯 Although the Book and DVD classes implement a Reservable interface, the reservation logic is fully implemented in the Library class .

