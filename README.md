# facebook-groups-post

This project have two scripts **save_groups**.py **post_groups**.py

The **save_groups**.py script is used to save the groups where you are a member in the data.json, searching them with specific keyword. This script is useful if you want to post in a lot of groups, because you can save the groups in the json file and use it in the **post_groups**.py script.


The **post_groups**.py script is used to post in spcific groups. In the data.json file you can save the groups where you want to post, and the script will post in all of them (a random post each time)

Warning: This script is not for spamming groups, is for post in groups where you are a member, and you want to post in a lot of groups at the same time. I am not responsible for the use that you give to this script.

# Install

## Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

## Installation

1. Clone the repo

   ```sh
   git clone https://github.com/vruttikalani30/facebook-groups-post-bot.git
   ```

2. Install python packages (opening a terminal in the project folder)

   ```sh
   python -m pip install -r requirements.txt 
   ```

3. Create a `.env` file and `data.json` file in the project folder.

# Settings

Update your chrome path in the `.env` file (note: the chrome path is the folder where chrome data its installed)

```js
CHROME_PATH = C:Users<<your-user-name>>AppDataLocalGoogleChromeUser Data
```

# Run

1. Before run the scripts, you need to login in your facebook account in chrome

2. (optional) Open the **save_groups**.py script with a code/text editor, and replace the "keyword" for search groups in the line 3

    ```python
    keyword = "python" # sample for search group where you are a member, about python
    ```

3. (optional) Run the **save_groups**.py script

    ```sh
    python __save_groups__.py
    ```

4. Open the "data.json" file, and add the groups where you want to post, and the text of the post in the "text" field

    ```json
        {
        "posts": [
            {
                "text": "text post 1",
                "image": "{image path}"
            },
            {
                "text": "text post 2",
                "image": "{image path}"
            },
            {
                "text": "text post 3",
                "image": ""
            },
        ],
        "groups": [
            "https://www.facebook.com/groups/sample-group-1/",
            "https://www.facebook.com/groups/sample-group-2/",
            "https://www.facebook.com/groups/sample-group-3/",
            "https://www.facebook.com/groups/sample-group-4/",
            "https://www.facebook.com/groups/sample-group-5/",
            "https://www.facebook.com/groups/sample-group-6/",
            "https://www.facebook.com/groups/sample-group-7/",
            "https://www.facebook.com/groups/sample-group-8/"
        ]
    }
    ```

5. Run the **post_groups**.py script

    ```sh
    python __post_groups__.py
    ```

6. Wait until the script finish, and enjoy your posts in the groups :

# Roadmap

- [x] Get all groups where you are a member related to a keyword
- [X] Single post per group
- [X] Choose a random post each time
- [X] Optional image in posts
