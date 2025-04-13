# LambdaTest Selenium Automation With Pytest

This project demonstrates a scalable and reliable automation testing framework using **Python**, **Selenium**, and **Pytest** on **LambdaTest**'s cloud-based Selenium Grid. It supports **cross-browser**, **cross-platform**, and **parallel test execution**, with clean and detailed HTML reporting.

---

## Thought Process

The goal was to create an automation framework that is:

- **Portable** (runs on any machine or Gitpod workspace)
- **Parallelized** (faster execution using multiple workers)
- **Cross-platform/browser** (test compatibility across systems)
- **Cloud-integrated** (runs remotely via LambdaTest)
- **Well-reported** (detailed HTML test reports)

Here’s how that was achieved:

1. **Framework Setup**:  
   Using Pytest, Selenium WebDriver, and LambdaTest integration for remote execution.

2. **Parallel Execution**:  
   `pytest-parallel` plugin allows concurrent test execution to save time.

3. **Cross-Browser Configurations**:  
   All test environment details are stored in `configurations.json`, making the framework easily extensible.

4. **LambdaTest Grid Integration**:  
   Remote browser sessions are created using capabilities passed to LambdaTest’s Selenium Grid.

5. **HTML Reporting**:  
   Post-execution reports are generated using `pytest-html` for visual debugging and result tracking.

6. **Issue Resolved**:  
   An earlier issue with missing environment variables (like `LT_USERNAME`, `LT_ACCESS_KEY`) was fixed. All tests are now passing as expected 🎉


---

## Prerequisites

- Python 3.9+
- Selenium
- Pytest
- LambdaTest account (with credentials)
- Gitpod (optional, for cloud dev setup)

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Abdullah0910/My_QA_Hackathon.git
cd My_QA_Hackathon

## 2. Set Environment Variables
set LT_USERNAME=abdullah.goodsamaritan
set LT_ACCESS_KEY=LT_C47INsDKvWIWau0GxpVlsRShaHOq2KzyCESsyu9UEUspcNA

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Run the Tests
pytest
## Lambdatest ID : XHQBU-ZPKP3-2BPSN-6KXMG