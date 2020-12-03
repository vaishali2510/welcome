# Welcome to DS-542 - Python in Data Science

## Introduction

<!-- Introducing the class, basic information on this repository -->

You made it! This is our start of a journey for the next few months!

This repository is your guide and orientation of the way we will be doing things in this class! In this repository, we will go over on GitHub, and basic use of python. You can use this place as a guide to find useful links related with this class.


## Concepts & Tools 

<!-- Concepts needs to be covered before getting into class content -->

Things you will need to get yourself familiar with. Following is the stuff you need to be prepared for to fully cooperate on this class.

### Git

<!-- The version control system -->

The assignments are stored and shared using [GitHub](https://github.com/) and we use [Git](https://git-scm.com/) to be able to version and interact with our repositories.

My recommendation is go over the following stuff.

- Your first steps towards Git, [Learn to use Git](https://guides.github.com/activities/hello-world/)
- Learn GitHub and Git using GitHub Lab, [Github Lab](https://lab.github.com/)
- Useful to understand how Git works, [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- Useful to understand how GitHub works, [Github Flow](https://enterprise.github.com/downloads/en/-github-flow-cheatsheet.pdf)
- Useful for your README.md files, [Github Flawored Markdown Cheat Sheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)
- Protips from Data Scientist at GitHub, [Tips, tricks, hacks, and secrets from Alyson La](https://github.blog/2020-04-23-github-protips-tips-tricks-hacks-and-secrets-from-alyson-la/)
- A simple git learning experience with a desktop app, [Git-it (Desktop App)](https://github.com/jlord/git-it-electron)
- A set of tutorials, [Get Git Right by Atlassian](https://www.atlassian.com/git)
- Overwhelmed by git command line, what about an app? [Sourcetree](https://www.sourcetreeapp.com/)

### Development Tools (IDEs)

<!-- VSCode and advantages -->

My favorite, bittersweet tool, [Visual Studio Code](https://code.visualstudio.com/), use it and you'll love it!

Install VSCode to your computer. Add the following extensions as well.
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) a new language server from Microsoft.
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) to enable intellisense, environment management, etc.
  - [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) for getting used to Markdown syntax.
  - [Live Code](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) to interact with each other.

Even tough are a lot of online resoources available to make the most out of VSCode, recently Microsoft introduced a new set of articles to [learn to code with Visual Studio Code](https://code.visualstudio.com/learn). **Utilize this** to get yourself familiar with VS Code and understand why tools like VS Code are much better than just a text editor.

There are alternatives of course, you are welcome to use those as well. The point is an IDE will make your life much easier if you choose to use one!

Alternatives

- [Atom](https://atom.io/)
- [Notepad++](https://notepad-plus-plus.org/) (I use it as an advanced Notepad, rather than an IDE) 
- [Sublime](https://www.sublimetext.com/)
- And many, many more over [here](https://www.google.com/search?q=integrated+development+editor).

Development tools from your browser!

- [Your instant dev environment in GitHub](https://github.com/features/codespaces)
- [An instant IDE and prototyping tool for rapid web development.](https://codesandbox.io/)

### Code Sharing Platforms (GitHub)

<!-- GitHub in brief -->

[GitHub](https://github.com/) is how people build software. It has over 100 million repositories hosted in its platform as of August 2019, and its an essential tool for collaboration and sharing.

- [Introduction to GitHub, by GitHub](https://lab.github.com/githubtraining/introduction-to-github)
- [An Introduction to GitHub by US Government!](https://digital.gov/resources/an-introduction-github/)
- [A Dead Simple Intro to GitHub for the Non-Technical](https://medium.com/crowdbotics/a-dead-simple-intro-to-github-for-the-non-technical-f9d56410a856)
- 
### Python

<!-- THe programming language we will be using a lot, a lot. -->

In this course, we use Python. You can use either [standard python](https://www.python.org/), or [anaconda distribution](https://www.anaconda.com/distribution/), up to your preference.

It is better to know Python syntax, even tough we will be covering it in the class.

- Learn the syntax, [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)
- Online Tool to Learn Python, [learnpython.org](https://www.learnpython.org/)
- A rather broader place to learn Python, [Geek for Geeks](https://www.geeksforgeeks.org/python-programming-language/)

### Google Colab

Colaboratory is built on top of Jupyter Notebook. 

- [basic_features_overview.ipynb](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
- [welcome.ipynb](https://colab.research.google.com/notebooks/welcome.ipynb)

## How You Will Do Assignments

We use Github Classroom for assignments. Basically, how it works is described in down.

1. I give you a link.
2. You click on a link, and you are hacked, and I demand for a small randsom!
3. Ignore the second step, you click the link, it will automatically create a repository for you under our GitHub webpage.
4. You download this repository using `git clone https://github.com/..../welcome.git`.
5. You work on the assignment, do a few commits, and `git push` it to GitHub.
6. When you are done with the assignment, you go back to your repository, and **download** it as ZIP, and upload it to the [blackboard](https://saintpeters.blackboard.com/).
7. I read it after the deadline passes, and give you a big `0`.
8. Ignore the 7th step, you will be graded properly.

We will also have an online interactive book for some assignments. Using [Runestone](https://runestone.academy/), we will utilize interactivitiy on the textbook level. I created a course for our class, you should [register](https://runestone.academy/runestone/default/user/register) to Runestone and then [find our course](https://runestone.academy/runestone/default/courses), named as `DS-542`.

## Practices

### Collaboration

<!-- Introducing students with branching, PRs, etc -->

As part of some assignments and projects, we will have to collaborate on the same repository. To do this we will go over how to do this.

``` py
from greeter import greet

# greets participants!
greet.greet_people()
```

You will learn how to contribute on a team project, and using a [Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request), we will merge our hardwork into a single repository.

### Grading

<!-- Introductory grading example with python -->

Grading will be based on syllabus. We will have assignments, midterm, and final project.

The letter grade of your final grade will be calculated using the following function. You can test this code by starting python from this folder's place.

``` py
from grader import calculate_letter_grade

# this can be you!
grade = calculate_letter_grade(
    assignments=[100, 100, 100, 90, 60, 100],
    final_project=100,
    midterm=90,
    return_grade=True
)

# gets A (97)
print(grade)
```

You can also run this script from command line through `python -c "import greeter; print(greeter.greet_people())"`.

## Todo List

<!-- A list of items for student to follow -->

- [x] You will mark things you did in this list, like this one.
- [x] Go over on this README file, entirely.
- [x] Go over the links in [the things you need to prepared for](#concepts--tools) section.
- [x] Review the [commit history](https://github.com/spu-python-203/welcome/commits/main) on this repository.
- [x] Try the grading function in [grading](#grading) section.
- [x] [Participate](https://github.com/spu-python-203/welcome/issues) in final project discussion!
- [x] Follow steps in [assignments](#assignments), and push your final changes to GitHub, to your repository. 

## Conclusion

<!-- The takeaway of this repository and whats next. -->

That's it! To a wonderful semester, 

Happy coding!
