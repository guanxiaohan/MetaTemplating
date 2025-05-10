# **MetaTemplating **
**An advanced Python templating engine for dynamic text generation, supporting placeholders, expressions, and scripting logic.**  

## 🌟 **Features**  
✅ **Dynamic Placeholder Substitution** – Supports expressions, variables, and default values  
✅ **Inline Computation** – Evaluates expressions like `<time.strftime("%m/%d/%Y")>`  
✅ **Variable Storage** – Cache results for reuse (`<UUID() |-> stored_uuid>`)  
✅ **Pre-processing Scripts** – Run initialization logic before parsing templates  
✅ **Batch Processing** – Generate structured text efficiently  

---

## 🛠 **Installation**  
```bash
pip install metatemplating
```

---

## 📌 **Usage Example**  

### **Basic Placeholder Substitution**  
```python
from MetaTemplating import Template

template_str = "Today's date: <time.strftime('%m/%d/%Y')>"
tpl = Template(template_str)
tpl.analyze_template()
print(tpl.fill_template())  # Outputs: Today's date: 05/10/2025
```

### **Variable Storage and Retrieval**  
```python
template_str = "Generated UUID: <UUID() |-> stored_uuid>\nThe second time: <$stored_uuid>"
tpl = Template(template_str)
tpl.analyze_template()
print(tpl.fill_template())
```

### **Using a Pre-script for Initialization**  
```python
script_template = """
|>ScriptBeforeTemplate
store("author", "John Doe")
|>EndScript
Written by <$author>
"""
tpl = Template(script_template)
tpl.analyze_template()
print(tpl.fill_template())  # Outputs: Written by John Doe
```

---

## 🎨 **Advanced Template Processing**  
MetaTemplating supports **custom templates**, **batch processing**, and **integration with external data sources**.

```python
data = {"score": 95}
template_str = "Score result on [time.asctime(time.localtime())]:\n<$name | DefaultName>: <$score>"
tpl = Template(template_str)
tpl.analyze_template()
print(tpl.fill_template(data))  # Outputs: Hello Alice, you scored 95 in the exam.
```

---

## 🤝 **Contributions**  
- Feel free to submit **pull requests** to improve functionality.  
- Report bugs or suggest features via GitHub Issues.  

## 📜 **License**  
MIT License – Open-source and free to use.
