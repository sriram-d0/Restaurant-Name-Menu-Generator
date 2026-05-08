# 🍽️ GenAI Restaurant Name & Menu Generator

An AI-powered web application that generates **creative restaurant names** and **menu items** based on a selected cuisine using **Streamlit**, **LangChain**, and **OpenAI LLMs**.

This project demonstrates how **Sequential Chains in LangChain** can be used to orchestrate multiple LLM prompts in a structured workflow.

---

## 🚀 Features

* 🎯 Generate unique restaurant names based on cuisine
* 🍜 Generate matching menu items automatically
* 🔗 Uses **LangChain Sequential Chains**
* 🧠 Powered by **OpenAI LLM**
* 🌐 Interactive UI using **Streamlit**
* 🔐 Secure API key handling with environment variables
* ⚡ Simple and beginner-friendly GenAI project structure
* 🧩 Easily extendable for more AI features

---

# 🖼️ Project Workflow

The application follows this workflow:

1. User selects a cuisine from Streamlit UI
2. Input is sent to LangChain helper module
3. LangChain executes:

   * Chain 1 → Generate restaurant name
   * Chain 2 → Generate menu items
4. OpenAI LLM processes prompts
5. Final response is returned to Streamlit UI
6. Generated restaurant name and menu are displayed

---

# 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **OpenAI API**
* **LLMChain**
* **SequentialChain**

---




# ▶️ Run the Application

```bash
streamlit run main.py
```

---

# 🧠 LangChain Workflow Explained

## Chain 1 — Restaurant Name Generation

Prompt:

```python
"I want to open a restaurant for {cuisine} food.
Suggest a fancy restaurant name."
```

Example Output:

```bash
Spice Symphony
```

---

## Chain 2 — Menu Item Generation

Prompt:

```python
"Suggest some menu items for {restaurant_name}.
Return it as a comma separated list."
```

Example Output:

```bash
Paneer Tikka, Butter Naan, Biryani
```

---

# 🔄 Sequential Chain Flow

```text
Cuisine Input
      ↓
Restaurant Name Chain
      ↓
Generated Restaurant Name
      ↓
Menu Item Chain
      ↓
Final Response
```

---

# 💡 Example Output

```yaml
Restaurant Name:
Foodies IN

Menu Items:
- Samosa
- Paneer Masala
- Butter Chicken
- Biryani
- Masala Dosa
```


---


# 📈 Future Enhancements

* 🌍 Support more cuisines dynamically
* 🖼️ AI-generated restaurant logos
* 🧾 Recipe generation
* 📍 Restaurant location suggestions
* 🎨 Better UI/UX design
* 🤖 Multi-agent LangChain workflow
* 🧠 RAG integration for recipe databases

---


# 📚 Learning Concepts Covered

* Generative AI Basics
* Prompt Engineering
* LangChain Chains
* Sequential Workflows
* Streamlit UI Development
* OpenAI API Integration
* Environment Variable Handling

---


# 👨‍💻 Author

## Sriram (Uday Sriram Dutta)

* 💻 Passionate about AI, GenAI & Full Stack Development
* 🚀 Exploring LangChain, LLMs, RAG & AI Agents

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and share it with others!
