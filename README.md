pytest → test_runner.py → behave → feature file → steps → page → selenium → browser

---
flow of execution:
---

1. pytest
2. test_runner.py
3. behave command triggered
4. environment.py (before_all)
5. .feature file (Gherkin scenarios)
6. before_scenario (browser starts)
7. step definitions (login_steps.py)
8. page object (login_page.py)
9. Selenium WebDriver (browser actions)
10. assertions (validation)
11. after_scenario (browser quits)
12. Allure results generated

---
running only feature file 
---

behave features/login.feature:2 --no-logcapture --no-capture

---
running specific tag in feature file
--- 
behave -k @login
behave -f allure_behave.formatter:AllureFormatter -o reports/
behave -f html -o reports/report.html

---
running only feature file with pytest
--- 
pytest test_runner.py --alluredir=results --tags @login
pytest test_runner.py