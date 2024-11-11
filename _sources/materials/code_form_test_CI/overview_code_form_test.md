# Clean, tested and reproducible code

Often overlooked but tremendously important: clean, tested and reproducible code is the basis for any type of computational work, no matter if in academia or industry. But what does this actually refer to, what does it entail and what tools can be used to make it easier/ensure quality?

## Topics 💡

In the following you'll find the `objectives` and `materials` for each of the topics we'll discuss during this session.

### Code formatting

Here's one scenario all of us have been in before, most likely countless times: we want to run an anlysis and get a script from a colleague that should exactly what we want. Sounds great, eh? However, upon opening it your joy starts to drastically diminish: the entire script, many hundreds of lines long, is basically unintelligable. There are no comments, a fast number of apparently random variables, huge blocks of code, etc. . Long story short: re-using and/or adapting this script will be a lot of work and maybe not even possible.

The same holds true for code you might find online in repositories or even tutorials, as well as the worst case: your own code from a while ago. You wrote this once and now you don't understand a single thing that's going on. How is anyone supposed to understand the content of files like `finalanalysis_final_2.py` or `runthisbefore_monday.py`?

It's just annoying, frustrating and not `FAIR`. So, isn't there anything one can do about that?

There is: `code formatting`!

#### Objectives📍

We will briefly explore and learn about the following topics:

- [Guidelines for Code Styling](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_formatting.html#guidelines-for-code-styling)  
- [Writing Human Readable Code](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_formatting.html#writing-human-readable-code)  
- [Code Styling Tools](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_formatting.html#code-styling-tools)  

#### Materials📓

Please navigate to the respective section in the `ToC` on the left or [click here](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_formatting.html#)

### Code testing

Here's another scenario many of us have encountered more times than we'd like to admit: we carefully write a `script`, everything seems to work perfectly, and we proudly share it with a colleague, in an open repository—or perhaps revisit it ourselves after a few months. Then, the dreaded moment comes. Someone runs the `code`, only to encounter mysterious `errors`, or it runs but produces results that make no sense. Everyone starts troubleshooting, `line` by `line`, only to realize that a single `function` doesn’t do what it’s supposed to, or that a critical `calculation` is misbehaving. In short, the `code` fails in ways that aren’t immediately obvious. It’s frustrating, time-consuming, and sometimes downright confusing.

The same scenario can apply to `code` you find online or even `code` that others depend on in `tutorials` or `open-source repositories`. Just because `code` works once doesn't mean it will continue to work or work in different scenarios or on different data. In the worst-case scenario, you don’t even know if the `code` is doing what it should because there's no clear way to check its behavior in different situations.

So, isn’t there something we can do about this?

There is: `code testing`!

#### Objectives📍

We will briefly explore and learn about the following topics:

- [Code testing - the basics](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_testing.html#code-testing-the-basics)  
- [Testing frameworks](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_testing.html#testing-frameworks)  
- [Code testing - different types of testing](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_testing.html#code-testing-different-types-of-tests)  

#### Materials📓

Please navigate to the respective section in the `ToC` on the left or [click here](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_testing.html#)

### Continuous integration

Imagine this: you’ve finally finished writing a `script` or a new `code feature`, and you `push` your changes to the respective `repository`. Now, it’s time to relax, right? Not so fast! Hours later, you receive messages from your collaborators and other people who want to use your `code` about bugs that appeared in it. It turns out your changes unintentionally broke other parts of the `project`, or they’re only working on your `setup` and failing elsewhere. Now, you’re faced with hours of troubleshooting—and possibly even a rollback.

This scenario also sounds very familiar, eh? Relying solely on local `testing` or manual checks before sharing `code` is time-consuming and often unreliable, especially when multiple people work on the same `codebase`.

But there is a solution: `continuous integration` (`CI`)! 

#### Objectives📍

We will briefly explore and learn about the following topics:

- [Continuous Integration basics](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/CI_CD.html#)  
- [GitHub actions](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/CI_CD.html#github-actions)  
- [Building workflows](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/CI_CD.html#building-workflows)  

#### Materials📓

Please navigate to the respective section in the `ToC` on the left or [click here](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/CI_CD.html#)
