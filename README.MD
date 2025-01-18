# **CLI Flow for Expense and Income Tracker**

#### **1. Welcome Screen**

- **Message**:
  - "Welcome to the Expense & Income Tracker!"
  - "Are you a registered user?"
    1. Yes
    2. No

#### **2. User Verification**

- **If "Yes" (Registered User)**:

  - Prompt: "Enter your username and password."
  - If authentication succeeds:
    - Message: "Welcome back, [username]!"
    - Show the main menu.
  - If authentication fails:
    - Error: "Invalid credentials. Please try again."

- **If "No" (New User)**:
  - Message: "Let's create your account!"
  - Prompt:
    - "Enter a username:"
    - "Enter a password:"
  - Confirmation: "Account created successfully! Please log in."
  - Redirect to login prompt.

---

### **3. Main Menu**

Once logged in, display the following options:

- "What would you like to do?"
  1. View Expenses & Incomes
  2. Add Expense
  3. Add Income
  4. Generate Summary
  5. Log Out
  6. Exit

---

### **4. Option Details**

#### **4.1 View Expenses & Incomes**

- **Action**:
  - Display a table with previous expenses and incomes.
  - Include columns like:
    - **Date** | **Type** (Expense/Income) | **Category** | **Description** | **Amount**
  - Message: "Here’s your current record."
  - Prompt: "Press Enter to return to the main menu."

#### **4.2 Add Expense**

- **Action**:
  - Prompt user for details:
    - "Enter date (YYYY-MM-DD):"
    - "Enter category (e.g., Food, Travel, Rent):"
    - "Enter description:"
    - "Enter amount:"
  - Confirmation: "Expense added successfully!"
  - Return to the main menu.

#### **4.3 Add Income**

- **Action**:
  - Prompt user for details:
    - "Enter date (YYYY-MM-DD):"
    - "Enter source of income (e.g., Salary, Freelancing):"
    - "Enter description:"
    - "Enter amount:"
  - Confirmation: "Income added successfully!"
  - Return to the main menu.

#### **4.4 Generate Summary**

- **Action**:
  - Ask user to choose a summary type:
    1. View summary for a specific month.
    2. View overall summary.
  - Display:
    - **For Monthly Summary**:
      - Total income and expenses for the selected month.
      - Categorized breakdown (e.g., Food: $200, Travel: $50).
    - **For Overall Summary**:
      - Total income and expenses.
      - Categorized breakdown.
  - Message: "Summary generated successfully!"
  - Prompt: "Press Enter to return to the main menu."

#### **4.5 Log Out**

- **Action**:
  - Save session data.
  - Message: "You’ve been logged out. Have a great day!"
  - Redirect to the welcome screen.

#### **4.6 Exit**

- **Action**:
  - Save session data.
  - Message: "Goodbye! See you next time."

---

### **Additional Features (Optional Enhancements)**

- **Password Reset**:
  - Option on the login screen to reset the password using security questions or a secret phrase.
- **Search Functionality**:
  - Search for specific records by keyword, date range, or category.
- **Budget Alerts**:
  - Notify the user when they exceed a predefined monthly budget.

---

### **Error Handling**

1. **Invalid Input**:
   - Message: "Invalid input. Please try again."
2. **Authentication Failure**:
   - Message: "Incorrect username or password. Please try again."
3. **Empty Records**:
   - Message: "No expenses or incomes found. Add some records first!"

---

### **Final Flow Recap**

1. Welcome Screen → User Verification (Login or Register).
2. Main Menu (View, Add, Generate Summary, Log Out, Exit).
3. Detailed functionality for each menu option.
4. Robust error handling to guide the user.
