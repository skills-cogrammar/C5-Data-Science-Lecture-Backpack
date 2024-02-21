## Case Study
We need to create a simple finance tracking application that allows a user to track their daily income and spending. The user should be able to save the information that they enter to a local file so that the information can be presisted. 

### Key Requirements 
- Add income 
- Add expense 
- Save to file

### Additional Requirements
- View expenses 
- View Income
- View Current Balance 


## Data

### Entity Diagram 

```mermaid
erDiagram    
    Entry {
        string id
        datetime date
        float amount
        string description
        string title
    }
```

--- 

### Class Diagram

```mermaid
classDiagram
    class JsonService{
        -connection string
        +write(entry)
        +get_all()
        +get(id)
    }    
```

```mermaid
classDiagram
    class SqliteService{
        -connection string
        +write(entry)
        +get_all()
        +get(id)
    }    
```

```mermaid
classDiagram
    class TransactionRepository{
        -connection string
        +add_transaction(transaction)
        +get_all()
        +get(id)
        +get_all_income()
        +get_all_expenses()
    }    
```

```mermaid
classDiagram
    class FinancialRepository{
        -connection string
        +get_current_balance()
        +get_balance_in_range(start, end)
    }    
```

----

## NOTES
Data generated using [Mockaroo](https://mockaroo.com/)