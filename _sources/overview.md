# Overview

Often overlooked but tremendously important: clean and reproducible code is the basis for any type of computational work, no matter if in academia or industry. But what does this actually refer to, what does it entail and what tools can be used to make it easier/ensure quality?

In this short [Neuromatch](https://neuromatch.io/) [Impact Scholars](https://impact-scholars.neuromatch.io/impact-scholars/intro.html) workshop, we will explore the respective basis, including:


- [Code formatting, styling and linting](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_formatting.html)
- [Code testing](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/code_testing.html)
- [Continuous integration](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/CI_CD.html)

These topics will be explored based on examples provided by the organizers with the option to also discuss examples brought by the participants. 

The workshop was first held virtually on November 11th-12th 2024.

All materials are published as a [JupyterBook](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch). 

We will further explain the aspects, as well as the `setup`, etc. below. For a precise outline of this workshop, please consult the respective [page](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/materials/code_form_test_CI/overview_code_form_test.html). 


## The framework and setup

The entire workshop will be conducted via the [Jupyter ecosystem](https://jupyter.org/), utilizing the [python programming language](https://www.python.org/) for all examples. All materials will be provided within the [Jupyter Book](https://jupyterbook.org/intro.html) format you're currently look, free for everyone to check and try out, as well as utilize further. To help folks that don't have any experience with these resources, we compiled a set of tutorials that participants can go through within the [prerequisite section](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/prerequisites.html). While this won't be enough to go past basic skills, we still hope it will be useful to familiarize yourself with core aspects that will help during the workshop. Each of these tutorials, as well as "main" materials will be in [jupyter notebooks](https://jupyter.org/) and contain a mixture of explanations and code and presented as a "slide show" during the workshop. They can be just viewed, or either run interactively via cloud instances (via [mybinder](https://mybinder.org/)) or locally. Depending on a given participant's computational resources and infrastructure, we provide multiple ways to participate in the workshop as outlined in the [Setup](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/setup.html) section.

## Instructors

You can find the main team below and get further information via clicking on the respective names. 

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/PeerHerholz">
        <img src="https://avatars.githubusercontent.com/u/20129524?s=96&v=4" width="100px;" alt=""/>
        <br /><sub><b>Peer Herholz (he/him)</b></sub>
      </a>
    </td>
  </tr>
</table>


```{admonition} How to address one another?
:class: dropdown
When contacting us, please refrain from using titles when addressing us and super formal language, using our first names is fine and it’s way more important that the content is respectful, fair and constructive (We aim for the same when we reply). However, please let us know if you have a preferred way of interacting with other folks, including how you would liked to be addressed, your pronouns and the level of formality.
```

### The details

Below you will find important details regarding the workshop, summarized in a compact form. Please consult and familiarize yourself with the information presented there prior to and/or within the first few days of the workshop. 

#### When and where

**November, 11th-12th 2024**, virtual via zoom. 

**Schedule:**

| 11/11/2024 | 12/11/2024 |
|:---:|:---:|
| Intro/Setup & Code formatting | Code testing & CI |

#### Can I use my calculator?

For this class you will need frequent access to a computer. None of the analyses that we will be doing will be very intensive, so this does not need to be a modern or "fast" computer. Still, it will need to be running a standard operating system like `Windows`, `Mac OS X`, or `Linux`. Unfortunately, tablets running mobile operating systems (`iOS`, `Android`) probably won't work for this purpose. If this is an issue for you, please get in touch with the instructor as soon as possible so that we can try to figure out a solution. Regarding software and installation thereof, please check the next section.

<p align="center"><iframe src="https://giphy.com/embed/DHqth0hVQoIzS" width="240" height="103" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><p align="center"><a href="https://giphy.com/gifs/maths-DHqth0hVQoIzS">via GIPHY</a></p></p>

#### How do I get all the software and do I have to apply for a loan to get it?

Don't worry at all. First, in order to help you get all the software required for the course, a [comprehensive installation instruction](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/setup.html) was compiled. In a step-by-step manner it guides you through the installation process, covering several `OS`: `Windows`, `Mac OS X` and `Linux`. Second, everything will be completely free of charge as we will only use publicly available [open-source software](https://en.wikipedia.org/wiki/Open-source_software). Why? Because teaching participants via [proprietary software](https://en.wikipedia.org/wiki/Proprietary_software) is just not fair and won't help anyone: participants have to obtain licenses or use those from the university (which usually doesn't have enough for everyone), leading to tremendous problems regarding inequity now and in the future. Additionally, [opens-source software](https://en.wikipedia.org/wiki/Open-source_software) can do everything, if not more, what [proprietary software](https://en.wikipedia.org/wiki/Proprietary_software) can and is furthermore usually better supported, tested and documented, creating a fantastic sense of community. 

<p align="center"><iframe src="https://giphy.com/embed/CTX0ivSQbI78A" width="240" height="177" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><p align="center"><a href="https://giphy.com/gifs/internet-computer-technology-CTX0ivSQbI78A">via GIPHY</a></p></p>

#### Where is everything?

All materials (slides, lecture demo notebooks, etc.) will be available on the [workshop's website](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/intro.html), i.e. the one you're looking at right now. Everything will be completely open and free to use, thus constituting an [open educational resource](https://en.wikipedia.org/wiki/Open_educational_resources) you are free to explore, enhance and share. Thus, this website and all materials will also remain up for the entire duration of the workshop and beyond, ideally to the end of the internet. The usage of this resource and the materials therein will be explained at the beginning and throughout the workshop.  

<p align="center"><iframe src="https://giphy.com/embed/c20UV66B7zCWA" width="240" height="155" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><p align="center"><a href="https://giphy.com/gifs/superman-phone-looking-c20UV66B7zCWA">via GIPHY</a></p></p>

#### Syllabus and Text

As noted above, this page serves as the syllabus for this course, with the precise outline indicated in the [respective section](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/outline.html). This syllabus is subject to change; please check-in frequently for learning about any changes to the syllabus.

Additional reading material might be added but will always be open & free with participants being informed about any addition.

<p align="center"><iframe src="https://giphy.com/embed/9dFvgd4ID6ne0" width="240" height="135" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><p align="center"><a href="https://giphy.com/gifs/community-nbc-ken-jeong-9dFvgd4ID6ne0">via GIPHY</a></p></p>

### Code of conduct

This course has a `Code of conduct`. Please inform yourself about the specifics by carefully reading through the [respective section](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/CoC.html).

<p align="center"><iframe src="https://giphy.com/embed/l5s71uAp3CzKwxwkoZ" width="240" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><p align="center"><a href="https://giphy.com/gifs/theoffice-nbc-the-office-tv-l5s71uAp3CzKwxwkoZ">via GIPHY</a></p></p>


### How to Get Your Question(s) Answered and/or Provide Feedback

It’s great that we have so many ways to communicate, but it can get tricky to figure out who to contact or where your question belongs or when to expect a response. These guidelines are to help you get your question answered as quickly as possible and to ensure that we’re able to get to everyone’s questions.

That said, to ensure that we’re respecting everyone's time and thus will mainly answer questions between normal working hours (M-F 9AM-5PM). The instructors are also going to do their best to stick to these working hours. However, they know that’s not when you may be doing your work. So, please feel free to post messages whenever is best for you while knowing that if you post late at night or on a weekend, you may not get a response until the next weekday. As such, do your best not to wait until the last minute to ask a question.

If you have:

- questions about course content - these are awesome! We want everyone to see them and have their questions answered too, so either use the [hypothes.is](https://web.hypothes.is/) plugin, the `e-mail` list or the [GitHub repository](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/issues).

- a technical assignment question - come to office hours. Answering technical questions is often best accomplished ‘in person’ where we can discuss the question and talk through ideas. However, if that is not possible, post your question the [GitHub repository](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/issues). Be as specific as you can in the question you ask. And, for those answering, help your classmates as much as you can without just giving the answer. Help guide them, point them in a direction, provide pseudo code, but do not provide code that answers assignment questions.

- been stuck on something for a while (>30min) and aren’t even really sure where to start - it can be frustrating and it may not always be obvious what is going wrong or why something isn’t working. That’s OK - we’ve all been there! IF you are stuck, you can and should reach out for help, even if you aren’t exactly sure what your specific question is. To determine when to reach out, consider the 2-hour rule. This rule states that if you are stuck, work on that problem for an hour. Then, take a 30 minute break and do something else. When you come back after your break, try for another 30 minutes or so to solve your problem. If you are still completely stuck, stop and contact us (via Email or [GitHub repository](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/issues)). If you don’t have a specific question, include the information you have (what you’re stuck on, the code you’ve been trying that hasn’t been happening, and/or the error messages you’ve been getting).

- questions about course logistics - first, check the [overview](https://peerherholz.github.io/Clean_Repro_Code_Neuromatch/overview.html). If you can’t find the answer there, first ask a classmate. If still unsure, make use of the [GitHub repository](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/issues).

- something super cool to share related to class or want to talk about a topic in further depth - feel free to post it, contact the organizers/instructors. 

- some feedback about the course you want to share anonymously - If you’ve been offended by an example, really liked or disliked a session, or wish there were something covered in the workshop that wasn’t but would rather not share this publicly, etc., please reach out via Email

### Acknowledgements

Several parts of this section are directly taken or adapted from [Alexander Huth's Neuro Data Analysis in Python syllabus](https://github.com/alexhuth/ndap-fa2020) licensed under a [BSD-3-Clause License](https://github.com/alexhuth/ndap-fa2020/blob/master/LICENSE) and [Shannon Ellis' COGS 18: Introduction to Python](https://cogs18.github.io/assets/intro/syllabus.html). 