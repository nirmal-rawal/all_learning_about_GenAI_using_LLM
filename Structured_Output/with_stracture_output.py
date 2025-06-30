from langchain_community.llms import Ollama
import json

llm = Ollama(model="mistral")

prompt = """
Analyze the following review and return a JSON object with two fields: "summary" and "sentiment".

Review:
"Django is a high-level Python web framework that has been a popular choice among developers for over a decade. Designed to help developers build robust, secure, and scalable web applications quickly, Django follows the “batteries-included” philosophy — offering a wide array of built-in features right out of the box.

One of Django’s strongest points is its rapid development capability. Thanks to its built-in admin interface, ORM (Object-Relational Mapping), and ready-to-use authentication system, developers can go from idea to deployment in significantly less time compared to many other frameworks. This makes Django an excellent choice for startups, academic projects, and even full-fledged enterprise solutions.

Another major advantage is Django’s security features. It protects against many common vulnerabilities like SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), and clickjacking. With security being a major concern in today’s web applications, Django helps ease a developer’s burden by handling much of it internally.

The Django community is also a big plus. It is mature, well-documented, and highly active, which means finding solutions to problems, accessing learning resources, and integrating third-party packages is usually easy and smooth.

However, Django is not without its downsides. For one, its monolithic architecture can be limiting for projects that require a more flexible or microservice-based design. The framework is tightly coupled in many aspects, which makes replacing or customizing certain components (like the ORM or templating engine) a bit of a challenge.

Additionally, Django can sometimes feel bloated or opinionated, especially for smaller or simpler projects. Developers coming from lightweight frameworks like Flask might find Django’s structure overly complex or too rigid. The “Django way” of doing things doesn’t always align with every project’s needs, especially when flexibility and minimalism are top priorities.

Another common criticism is its performance in real-time or asynchronous use cases. While Django now supports async views and middleware to some extent, it is still fundamentally synchronous. Frameworks like FastAPI or Node.js may be better suited for applications that rely heavily on asynchronous tasks, such as real-time messaging or high-frequency API calls.

In conclusion, Django is a powerful, mature, and feature-rich framework that excels in delivering fast, secure, and scalable web applications — especially when following conventional web architecture. However, for developers looking for more modular, lightweight, or asynchronous solutions, Django may not always be the best fit. Like any tool, its usefulness depends entirely on the project’s goals and the developer’s preferences."

Respond only in this format:
{
  "key":"...",
  "summary": "...",
  "sentiment": "...",
  "pros":"",
}
"""

response = llm.invoke(prompt)

# Parse the response as JSON
try:
    result = json.loads(response)
except json.JSONDecodeError:
    result = {"error": "Could not parse response as JSON", "raw_output": response}

print(result)
# print(result['summary'])
# print(result['sentiment'])
