import subprocess

def test_behave():
    result = subprocess.run(
        "behave -f allure_behave.formatter:AllureFormatter -o reports/",
        shell=True
    )
    assert result.returncode == 0
