[StripTeaser Blog](https://strip-teaser.herokuapp.com/) is designed as a place where fans of the ninth art will be able to write sneak peeks, and reviews, about different comic releases to promote and popularize comics. The idea itself came from being a comic book lover and collector myself. The name of the blog comes from a comic strip (in some countries a comic is called just a strip ([An editor named Dušan Timotijević named the new art form "strip", after English "comic strip"](https://en.wikipedia.org/wiki/Serbian_comics)), and with a play on words I came up with a slightly provocative name but also an attractive name.

[Here you have a live version of the project.](https://strip-teaser.herokuapp.com/)  

---  

## Table of Contents

1. <details>
   <summary><a href="#ux">UX</a></summary>

   - [Visitor Goals](#visitor-goals)
   - [Business Goals](#business-goals)
   - [User Stories](#user-stories)

   </details>
   
2. <details>
    <summary><a href="#visual-design">Visual Design</a></summary>

      - [Wireframes](#wireframes)
      - [Colors](#colors)
      - [Fonts](#fonts)
      - [Icons](#icons)

</details>

3. <details>
   <summary><a href="#styling-formatting-and-features">Styling, Formating and Features</a></summary> 
    
    - [Future Features](#future-features)

</details>

1.  <details>
    <summary><a href="#validation-and-testing">Validation and Testing</a></summary>
    <ul>
    <li><a href="#validation">Validation</a></li>
    <li><a href="#testing">Testing</a></li>

    <li>
    <details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Fixed Bugs](#fixed-bugs)
    </details>
    </li>
    </ul>

</details>
  
5. <details>
    <summary> <a href="#deployment">Deployment</a></summary>

      - [Local Deployment](#local-deployment)
      - [Heroku Deployment](#heroku-deployment)

</details>
  
---  
  
## UX


### Visitor Goals  

The target audience for [StripTeaser Blog](https://strip-teaser.herokuapp.com/) are:  
- People who are interested in comics and caricature art.
- People who like to read a quality and interesting reviews.
- People who like to express their opinion through writing reviews.
- People who want to find out if the comic book they are interested in buying is suitable for their affinities.


### Business Goals  

The Business Goals of [StripTeaser Blog](https://strip-teaser.herokuapp.com/) are:  
- To gather a group of quality authors of reviews.
- To provide quality reviews of comics both new and old.
- To become a relevant factor in the evaluation of comics in the future.
- To become an online shop, when a certain number of authors and readers gather.


### User Stories  

- As a **Site Admin** I can **approve or disapprove posts** so that **I can filter out the irrelevant posts**
- As a **Site Admin / Registered User** I can **use Rich Text Editor** so that **I can style my blog posts, add images and links**
- As a **Site Admin / Owner** I can **have neat code with comments** so that **other developers can quickly figure out what it's for**
- As a **Site Admin / Owner** I can **have ReadMe** so that **I can provide enough documentation and guide for other developers who are interested in project**
 - As a **Site User** I can **register account** so that **I can add a short biography and avatar, so that the readers know something about me as author**
 - As a **Site User** I can **view a list of comics** so that **I can select one to read about comic book release specs**
 - As a **Site User** I can **view a list of posts** so that **I can select one to read and see exactly which edition is being written about**
 - As a **Site User** I can **search the blog** so that **I can find what I'm interested in based on the comic's name, author, or content keyword**
- As a **Site User** I can **create, read, update and delete comments** so that **I can leave a review opinion as well as see other readers' review ratings** 
- As a **Site User / Registered User** I can **read news about  comics** so that **I am always updated with latest releases and announcements** 
 - As a **Registered User** I can **create, read, update and delete comics with detailed issue spec** so that **I or other members can write reviews for it, and visitors and collectors have an accurate insight into which product they are talking about**
 - As a **Registered User** I can **create, read, update and delete posts** so that **I can promote comics and give my opinion on certain releases**
- As a **Registered User** I can view custom error pages, example 404 so that **I can easily understand and navigate through them**
 - As a **Registered User** I can **send messages to authors of the review** so that **I can get in touch with them more easily** 
 - As a **Registered User** I can **reset password** so that **I don't have to create a new account in case I forget my password, but simply reset it** 
 - As a **Registered User** I can **participate in polls** so that **I and other can use the results to announce the best comics for different criteria**  

---  

## Visual Design


### Wireframes

- The initial project wireframes. As they are created in the early planning stages, they may differ from the final project.  


### Colors

- For the design, I had planned to create a blog with a clean look, so, at the very beginning, I decided that white color prevails (for a future feature of the site, a dark version will be implemented). In order for the site not to be too sterile and monotonous, I decided to assign different colors to details such as buttons, borders, and background animation elements, and in this way, the site becomes more dynamic and interesting.  
- The color palette I decided on is [eBay](https://www.ebay.de/) colors. The idea came while shopping on the site.  



### Fonts
- 



### Icons

-  As the main icon, which was also used as a favicon, it was downloaded from the [Looka](https://looka.com).  

- I used to generate the favicon icon [Favicon Generator](https://www.favicon-generator.org/).  


- The others that were used for buttons and social links are from the [Font Awsome](https://fontawesome.com/). I tried to use icons that suggest what the button action is (for example, the trash can for the Delete button).  

---  


## Styling, Formatting and Features   


### Styling, Formatting, Features
- I wanted the design of the site to be clean, so the white color prevails, and to gain interest and dynamism, colors were inserted for certain elements. And I stuck to that concept for the entire site.
- The technologies I used to create the site are: HTML, CSS, JavaScript, [Django](https://www.djangoproject.com), [Python](https://www.python.org/), [Bootstrap](https://getbootstrap.com), [PostgreSQL](https://www.postgresql.org/)
- Although Bootstrap was used for styling, I tried to add custom CSS and JavaScript so that the site would not look generic but a bit more unique.

- To implement the paginator I used the following source: [How to implement a paginator in a Django Class-based ListView compatible with Bootstrap 5](https://ourcodeworld.com/articles/read/1757/how-to-implement-a-paginator-in-a-django-class-based-listview-compatible-with-bootstrap-5)
- I restricted access to unauthenticated and unauthorized users with the Django authentication system by implementing @login_required decorator, LoginRequiredMixin and UserPassesTestMixin with custom test functions([Django docomentation](https://docs.djangoproject.com/en/4.2/topics/auth/default/)).
- I also applied this protection principle to other parts of the site where it was necessary to limit access to unauthenticated and unauthorized users.

#### Home Page
- The first thing I wanted users to encounter were is a welcome message with a short introduction about the site itself, what the user can find, and what we have planned for the future.
- As I mentioned I used the colors of the four basic eBay colors and to make the site more alive I used this tutorial to create a background animation ([Animated Background with Pure CSS and Html | No Javascript no Jquery](https://www.youtube.com/watch?v=qx7pSLjLNQA&list=PLwJhhWUZudKp7QPVALB_kXUyzj8cBB__L)).
- And to make it even more lively, I used the JavaScript `Math.random` method so that every time the page is loaded, the squares get random colors.

![Home Page]()

- The navigation bar is a Bootstrap navbar that has been modified for the needs of the project.

![Navbar]()

- The title itself with the logo is a link to the home page.
- I decided to highlight, in my opinion, important elements in yellow.

![Members]()

- The search functionality is limited to searching the post content itself, titles, authors of posts, writers and artists of comics, as well as publishers. Because I thought that these are the most important things that could interest the reader.
- I achieved the functionality with the help of an article from [Stackoverflow](https://stackoverflow.com/questions/13416502/django-search-form-in-class-based-listview).

![Search]()

- The search results page is simple with an appropriate heading.

![Search Results]()

#### Blog
- When designing the Blog List page, I decided to display four posts, so that the page would not be crowded and the user would have more attention when there is less content.
- So that the posts themselves would not be boring, I decided to follow the order of eBay colors and assigned each post a button color and border with a box shadow in the order red, green, blue, and yellow. I implemented this with a simple JavaScript solution.

	```const borderColors = ['red', 'green', 'blue', 'yellow'];  
    const cards = document.querySelectorAll('.card');   
	cards.forEach((card, i) => {.  
	    const randColor = borderColors[i % borderColors.length];
	    card.classList.add(randColor);
	});
    ```

![Blog Page]()


- I also wanted the Add New Review link to be available to registered members of the site, and I decided to position it just below the heading.

![Add New Review]()

- I decided that the first option for writing a review would be to choose a comic book to write about.
- And immediately after that, I offer the site member to add a new comic about which he wants to write if it does not already exist in the database.
- The other fields are basic, typical blog post fields such as title, body content, and image.
- 
![Write New Review]()

- What I should add in the next version is the Excerpt field, instead of that field I used the django filter `truncatewords`, which can sometimes cause unwanted results if the introduction is too short and there is too much empty space after it.


- So that the posts themselves could be nicely formatted, to add subtitles, images, I decided to implement the Rich Text Editor and I added a `safe` filter to render the content properly.
- I decided on CK-Editor because of easy and fast implementation, which I achieved with the help of [documentation](https://django-ckeditor.readthedocs.io/en/latest/) and this [video](https://www.youtube.com/watch?v=mF5jzSXb1dc).  
  
![CK Editor]()

- To upload an image, I used CloudinaryFileField ([with the help of this article I implemented it in this project](https://jszczerbinski.medium.com/django-web-app-and-images-cloudinary-straightforward-study-ae8b5bb03e37) and [this one](https://support.cloudinary.com/hc/en-us/articles/202520762-Uploading-assets-and-keeping-their-original-filenames)), which has, next to the image selection field, a field that displays a link to the image that is currently being used.
- For all forms I used [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) and for the field the currently selected image did not display the image address (problem probably caused by crispy-forms). Since the user already sees the selected image or avatar, I decided to target that field with a css selector and set display to none.

![Currently Field Hidden]()

- Also, after a successfully created post and for every other successfully created content, the user receives a django success message, which was implemented with the help of Code Institute I Think Therefore I Blog.  


##### Blog Post
- For the display of the blog post itself, I decided that in addition to the content of the post itself, a link to the author's profile, which can only be visited by registered users, should be available.
- And also a card on the side with the technical data of the edition being written about.

![Blog Post non Logged In]()


- The author of the post itself has links available at the bottom to upgrade or delete posts.

![Blog Post Logged In]()

- For the upgrade page, I simply used the same form as for creating a new one just prepopulate with content details.

- In case the user wants to delete the post, he must first confirm in order to avoid accidental deletion.


#### Strips / Comics
- For the list of available comics for review, I decided to follow the design of the blog page, increasing the number of objects to six displayed on one page.

![Strips / Comics Page]()

- For just creating a new comic, I decided on the technical data of the comic that I considered the most important, although there is room to expand and even divide it into several models.
- For fields like Coloring and Binding, I defined the possibility of selection in the model itself.
- While for countries I used a package [django-countries](https://pypi.org/project/django-countries/).
- And for years I used the [stackoverflow solution](https://stackoverflow.com/questions/49051017/year-field-in-django).
- The same concept is used for the image field as for the blog post image.

- The first thing a user sees is the cover of comic, the title and the name of publisher, and clicking the Details button reveals the rest of the information, for this solution I used Bootstrap collapse.
- The card itself shows all the technical information about the issue and I purposely made it narrow and long to resemble a 'strip'.

![Strips Card Logged In]()

![Strips Card Non Logged In]()

- Since I think it's pretty clear like this, I decided not to create a separate page for individual comics, but left it like this because the content is not extensive and yet it seemed clear to me.
- For the upgrade page, I simply used the same form as for creating a new one just prepopulate with content details.

![Strips Update Form]()

- In case the user wants to delete the post, he must first confirm in order to avoid accidental deletion.

![Confirm Delete]()


#### Members
- It is meant to be highlighted, in this case in yellow to emphasize importance. There you can find all the features for members of the site.
- Sign In from the page has a fairly simple design and uses the Django built-in login functionality, with a query if the user is registered at all and a link to the registration page.

![Sign In]()

- The Sign Up page functionality itself also uses it Django built-in login functionality.
- Unlike the basic registration page, fields for email are added as mandatory, first name, last name as additional fields.
- And it also has a query whether the user is already registered and if so a link to the Sign in page.


![Sign Up]()


- In addition to the basic personal data, I decided to extend the User model with additional information about registered members such as a short biography, location and avatar.
- I deliberately did not decide to set a default avatar, because I did not want to impose on the members or offend someone if I set as a default avatar that they do not like.
- For the display of the profile card itself, I decided to follow the concept of the site and the same as for the update page and the delete button.
- With that I added a link to the email of the users profile.



- I used a modal for Sign Out, I got the idea from this channel [Django Mastery](https://www.youtube.com/@djangomastery) and plan to implement it in future versions of the site for all confirmation queries.
-- slika sign out modal





#### Footer
- The footer itself is simple with copyright text and site logo.
- And the year that is updated with JavaScript.

![Footer]()


### Future Features  

- Add search filters
- Add division by genres
- Add option to add image gallery for posts
- Add an online comic shop
- Adding social links, as well as youtube in footer