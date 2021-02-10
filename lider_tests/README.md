# Test Task for a Position Engineer in Test Automation

Test cases in this project can be executed by python interpreter 3.9 and higher, and chrome browser version 88 and higher.
All the necessary modules are listed in the requirements.txt file.

## Description

The project contains 3 test classes with 1 test per class.

yandex_test.py contains a UI test case which opens 'www.yandex.ru' and login with credentials stored in data.yandex_data.py. 
Then it checks that inbox mail folder is opened and username is displayed near with a user logo.

google_test.py contains a UI test case which searches a coffee machine, checks a number of result links (which includes links with advertisement)
and checks if a target link (set up in data.google_data.py file) is present among these links. 
(I added Moscow to the end of the search message because in my case google shows result from Belarus firstly.)

reqres_test.py contains an API test case which checks that a response from ENDPOINT (can be set up and changed in data.reqres_data.py)
is successful (has a status_code 200) and there is no name "Janet" in the result json. 
(I added this check different from the check in the task because my json doesn't contain 'first_name' key or any key with a value 'Janet'.)

## Installation

Use git clone command to copy this repository to your local folder.

## Usage

You can run tests by set up Pycharm configuration with the necessary file with tests.
Or you can run tests from the terminal:

```python -m unittest yandex_test.YandexTestCases.test_login```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

No license.