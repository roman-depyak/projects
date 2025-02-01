function TopicsPage(){
            return (
                <>
                    <h2>Web Development Topics</h2>
                    <nav class="local">
                        <a href="#servers">Servers</a>
                        <a href="#frontendDesign">Frontend Design</a>
                        <a href="#optimizingImages">Optimizing Images</a>
                        <a href="#favicons">Favicons</a>
                        <a href="#forms">Forms</a>
                        <a href="#express">Express</a>
                        <a href="#JavaScript">JavaScript</a>
                    </nav>
                    <article id="servers">
                        <h3>Web Servers</h3>
                        <p> A designated homepage serves as the default web page displayed when a person visits a website without specifying a particular file or resource in the <strong>URL</strong>. The homepage is a file, most commonly 
                            the file at path /index.html. For example, this is the name used by OSU Engineering's server software, the Apache web server. A server that uses a different name for its homepage is 
                            Microsoft's .NET platform, which uses the name default.html. Some other examples of possible names are index.js or index.php for the homepage.  
                        </p>
                        <p> When viewing the Inspector Network tab output screen on both a local computer and the web server the index.html, main.css, and main.js files are seen. When viewing the outputs, the general and 
                            response headers are seen. Under the general header, the request URL, request method, and status code, and IP address can be viewed. The GET method is seen because data are being retrieved from 
                            the page. The status code is 200, which means that the page rendered. The IP address is the location of the index.html file on the web server. Under the response header the content type and 
                            date last modified are seen. The content type is HTML text and the date last modified is 10/6/24. One difference is that when viewing from the web server, the <strong>favicon.ico</strong> file is seen, but it 
                            cannot be seen when viewing from a local computer. Another difference between viewing from a local computer as compared to the web server is the URL of the index.html file. The URL when viewed 
                            from my local computer is file:///C:/Users/Owner/Desktop/index.html while the URL for the web server is https://web.engr.oregonstate.edu/~depyakr/a1-depyakr/index.html. 
                        </p>
                        <p>
                            The favicon.ico file has a status 200, which indicates that the request was successful. This is because the OSU server provides the favicon.ico file automatically, so I did not have to create 
                            or include it. The reason that the main.css and main.js files have a status 400 is because the server cannot process the request. This is because I did not create nor include main.css or main.js 
                            files in my a1-depyakr folder; the server cannot access these files because they are referenced, but they do not exist. 
                        </p>
                        <p>
                                The URL to my web file is https://web.engr.oregonstate.edu/~depyakr/a1-depyakr/index.html. The scheme is https://. The subdomains are web.engr and the domain is oregonstate.edu. The path to 
                                resource is /~depyakr/a1-depyakr/index.html. 
                        </p>
                    </article>
                    <article id="frontendDesign">
                        <h3>Frontend Design</h3>
                        <p> The goal of <strong>frontend design</strong> is to create the most appropriate experience for the users of a website. The main facets of frontend design include the visual design of a webpage, the GUI, and the user's 
                            interactive experience. An appealing visual design involves a consistent color, font, typography, photography, icon, and illustration scheme. A well-designed website will have a navigation system which is 
                            intuitive for first time users.
                        </p>
                        <p>
                            These are the Five E's of Usability.
                        </p>
                        <dl>
                            <dt>Effective</dt>
                            <dd>The first of the five "E"s of usability stands for effective. This is concerned with the user's ability to end up with an accurate result. When using the website, the user's questions must 
                                be answered correctly. The website must help the user answer his or her questions and ensure that the reason the user came to the website is fulfilled. One example of an effective 
                                website is a user visiting a meteorology website to find out the weather forecast for the day and the website reveals the temperature will be 75 degrees and the sky will be clear all day.</dd>

                            <dt>Efficient</dt>
                            <dd>An efficient website allows the user to perform and complete tasks in the least number of steps. The goal of an efficient website is for the user to get results quickly.
                                Some hallmarks of an efficient website are an intuitive navigation system, results are quickly found via search, easy to read, concise, and well-structured. 
                                An example of an efficient website would be a user going to a store's website to find their locations and using the search bar to quickly find the closest store location.</dd>

                            <dt>Enjoyable</dt>
                            <dd>This is concerned with how enjoyable the website is to use for the user. The website must be engaging for the user. One factor that can affect a user's enjoyment is 
                                the website appearing uncluttered as compared to a website dense with text. Other factors include graphics, motion design, and information chunking. 
                                One example of an enjoyable website would be a children's educational game website having a brightly colored theme, cartoon animations, and easy to read words so that children are more enticed to learn
                                and play games on the website due to a welcoming and cheery theme as well as familiar cartoon characters greeting the child on the home page.</dd>

                            <dt>Easy to Learn</dt>
                            <dd>It is paramount for new users to be able to navigate and quickly learn the website. An easy to learn and easy to navigate website allows users to immediately understand how to locate and achieve
                                their goal through clicking and searching. Another crucial part of an easy to learn website is the user being able to remember how to navigate the website upon their next visit. 
                                One example of an easy to learn website would be a user going to a grocery store's website for the first time to purchase groceries from his or her home; as the website
                                is easy to learn and navigate, the user is quickly able to search for, find, and add the desired foods to the online shopping cart. Lastly, the user is able to quickly learn how to purchase the 
                                groceries from the cart and have them delivered to his or her house.</dd>

                            <dt>Error-free</dt>
                            <dd>The goal of an error-free or error-tolerant website is to avoid accessibility and availability issues. This means error prevention. This is done by learning what users' common errors are and then 
                                leveraging this information to help mitigate similar problems in the future. One example of an error-tolerant website is a restaurant's website using a ZIP code lookup API to ensure
                                that a user's order is being delivered to the correct address and prompting the user for confirmation to ensure that the user did not enter an incorrect address for the food delivery. </dd>
                        </dl>

                        <p> The purpose of the <strong>header element</strong> is so the user knows that they are on the same website even if they go to a different webpage. A header element usually contains a website name, publisher, and a slogan. 
                            The purpose of the <strong>nav</strong> element is to take the user to different webpages. The main element is used to demarcate the main content of the webpage from other content. Content that is typically part of the 
                            main element includes stories, galleries, and tutorials. The <strong>section element</strong> is used to group content. Content that is all related or has something in common will be grouped into a section element.
                            Within a section, the headline &lt;h1&gt; is used to describe the type of content will be within that section. If all of the content within the section element is not related,
                            then the section element should not be used. The article element is typically used inside the section element. The article element is used to separate a particular topic from the rest of the similar 
                            content within the section element. One example is if the section was sports stories, then soccer could be an article. When many articles are within the same section, an ID selector
                            can be used to allow for different styling and separate the articles from one another. Using an ID has the added benefit of allowing the anchor to land on them when jumping from a different portion of the same page.
                            The footer element is typically located below the main element. The footer element contains legal information, contact information, and links to important pages. Additionally, headings
                            are used for a headline. This will appear as bolded and in a larger font when viewed on the website. Headings are in the form of a hierarchy with h1 being the highest level and h6 being the lowest level. 
                        </p>
                        <p>
                            This is how anchors work.
                        </p>
                        
                        <ol>
                            <li>An <strong>anchor</strong> links to external content by using its <strong>href attribute</strong>. The href attribute creates a hyperlink to an external website. When a user clicks the text, he or she will be taken to the external website specified
                                by the href attribute. </li>
                            <li>An anchor links to internal content by using IDs. When a tag has an ID attribute, its value can be used with a hashtag to define the resource. This allows for an anchor to land at the resource.</li>
                            <li>An Anchor links from page-to-page using its href attribute, which creates a hyperlink to a webpage using a URL and is used to specify where the link will take the user when clicked. The content enclosed 
                                within the opening and closing anchor tags should describe the link when a user clicks to visit it. </li>
                        </ol>
                    </article>
                    <article id="optimizingImages">
                        <h3>Optimizing images</h3>
                        <p>
                            There are six major image optimizing specifications. The first specification is a descriptive file name. The purpose of this specification 
                            is to  improve <strong>search engine optimization</strong>. The focus of this specification is to use descriptive yet concise file names 
                            so that search engine bots are better able to categorize photos for users searching for similar topics. The second specification is
                            small file size. The goal is to reduce file sizes to the smallest size possible as minimizing the file size allows for the shortest 
                            possible load time. When a user is going to a webpage they want images to load quickly as they do not wish to wait for large images to 
                            finish loading. Thus, reducing file size decreases load times and improves user experience. Two ways of achieving a smaller file size
                            include <strong>lossy compression</strong>, which uses approximations to discard some image data and may lead to pixelation,
                            as well as <strong>lossless compression</strong>, which does not negatively impact visual quality. The third specification is exact
                            dimensions. This is focused on cropping and reducing image sizes to fit the dimensions of space available on the web page.
                            Having a larger picture than space on the web page will lead to the image loading very slowly and a detrimental effect on user experience.
                            The fourth specification is correct file format. Ensuring that the correct file format is used with an image helps uphold visual quality
                            and allows for a better user experience. If the incorrect file format is used an image may appear illegible, blurry, or incorrect file 
                            size. The fifth specification is reduced resolution. The goal of reduced resolution is to provide appropriately sized images to the user.
                            Users can view a web page on a multitude of different devices, all with unique resolutions. Monitors typically range between 72 and 
                            300 pixels per inch, but smartphones have lower resolution screens and typically access the internet using data bandwidth. Typically
                            a website should provide desktop users with higher resolution images and smartphone users with lower resolution images. This helps
                            prevent slow load times for smartphone users and ensures that desktop users are able to view high resolution, visually appealing images.
                            The last specification is color mode. Color modes include hexadecimal, RGB, and HSL. RGB is used for .PNG, .JPG, .SVG, 
                            and WebP file formats. Indexed may be used for GIF or PNG. Color mode is vital because it determines how colors are displayed
                            in images for the user. If an incorrect color mode is selected for the wrong file type it may result in inaccurate color representation,
                            increased file size, or compatibility issues. This may result in the user viewing a visually unappealing image, slower load times, or
                            inability for the image to load. All of these negatively affect user experience and should be avoided. This can be done by choosing
                            the correct color mode for the associated file type or types.     
                            </p>
                            <p>
                            The <strong>file formats</strong> appropriate for photos include JPG and WebP. JPG files are only used for photographic images. This file type
                            is typically too big for the web as photos of this file type usually have millions of colors, are very detailed, and are taken using
                            high-resolution cameras. When resized and compressed, these file sizes can be compressed down to small file sizes and remain 
                            a rectangular shape. It is important to note that higher compression reduces image quality. WebP files are also usually only used
                            for photographic images. They also compress down to small file sizes and remain rectangular. If an alpha channel is used, 
                            transparent backgrounds are possible. The file formats appropriate for line art include PNG, SVG, and GIF. PNG files may be
                            used for line art images, if the compression software is able to adequately compress the photo, but the photo may be pixelated.
                            SVG photos have crisp text and may be used for line art. GIF photos are most commonly used for line art. GIF files' edges anti-alias
                            which helps images appear more realistic. 
                            </p>
                    </article>
                    <article id="favicons">
                        <h3>Favicons</h3>
                        <p>
                            Browsers and devices use favicons to quickly identify a website in a browser tab, on a smartwatch, cellphone, tablet, or search engine 
                            results page, or website app by displaying the company logo or symbol in the correct size and file type. The company chooses a symbol or logo.
                            Then this symbol is modified to work well on many different devices. It is saved in multiple file formats to be used by different 
                            web browsers and devices. The browser is able to use the files, and then save the icon and anchor to a bookmark or favorites list as well as a 
                            device screen or search engine results list. Typically two or more versions are made of a favicon. A fancy favicon and a simpler favicon are 
                            typically made. 
                        </p>
                    </article>
                    <article id="forms">
                        <h3>Forms</h3>
                        <p>
                            There are six major goals of accessible forms. The first is to provide clear instructions above the forms and labels. This ensures that the user understands how to fill out the form correctly.
                            The second goal is to let users know why the data is being gathered and which fields are required. This ensures that the user understands which portions of the form they are able to skip and helps the user feel more comfortable as he or she may not wish to give away multitudes of personal information.
                            The third goal is to set the first field to autofocus. This helps for efficiency and user satisfaction as they do not have to worry about clicking inside a textarea to begin filling out information and instead can start typing on a keyboard or dictating into their device to fill out information.
                            The fourth goal is to ensure each form control can be filled in by using a keyboard. This ensures that users who are unable to use a mouse or trackpad are still able to fill out the form.
                            The fifth goal is to add tab indexing to complex forms. This ensures clarity and improves ease when filling out the form.
                            The final goal is to ensure validation messages are screen readable. This is so that visually impaired users are able to obtain the same information as everyone else after completing the form.
                            </p>
                            <p>The major tags are form, label and input. The form tag's attributes are action and method. The purpose is to specify where the request from the form should be sent and to specify the HTTP method to be used in the HTTP request sent when the form is submitted.
                            The label tag's attributes are for and id attributes. This helps ensure that the data submitted can be used after the HTTP response. The input tag has  a type attribute, which affects how the input tag behaves and is displayed.</p>
                            <p>The first major form style recommendations to improve usability is to add required status to tell users which fields are required. The second is to add autofocus to where the user should first start typing into the form. The third is to have a legend which helps describe its group of form controls.
                            All of these help the user with ease of filling out the form and help him or her better understand the form.
                        </p>
                    </article>
                    <article id="express">
                        <h3>Express</h3>
                        <p>
                            Node is a runtime environment for developing server-side and networking applications; Node Package Manager (npm) is a registry and command line tool for JavaScript software packages. It's a place to publish and install open-source Node.js code and projects. Express is a web framework which is used to build web applications and APIs. 
                            These three technologies can be used for developing JavaScript based web applications and APIs. 
                        </p>
                    </article>
                    <article id="JavaScript">
                        <h3>JavaScript</h3>
                        <p>
                            The main data types of JavaScript are number, Boolean, string, symbol, date, undefined, null, and objects. 
                            A number is a double-precision floating-point number. Numbers can be used to perform arithmetic operations. There are two types of 
                            Boolean values: true and false. When evaluating conditionals, JavaScript converts all values to true or false in order to evaluate the conditional.
                            In JavaScript, strings can be enclosed in either a single or double quote. Additionally, in JavaScript strings can also contain expressions. 
                            JavaScript has many packages to handle dates, such as Moment and Temporal. 
                            Undefined and null are both special values used to indicate the absence of a value. 
                            In JavaScript, an object is a set of name-value pairs. A programmer can add, read, update, and delete these name-value pairs of an object.
                        </p>
                        <p>
                            Objects are used to store name-value pairs. These are also known as properties of an object. These properties can be added, updated, read, and deleted. 
                            One type of object is an array. Arrays can be used to store data as elements of the array and quickly access elements by using 0-based indexing.
                            The values of an array can be of any data type. 
                            JSON is used as a way to transfer data between applications. JSON allows for data to be exchanged between two applications even if the applications are 
                            written in different languages, as the JSON format is language independent. JSON is able to map an object to a string and create an object from a string in the JSON format.
                            Both of these utilities allow for JSON to transfer data from one project to another, independent of the coding language of either project. 
                        </p>
                        <p>
                            Conditionals allow a program to branch and make decisions based on whether an expression is evaluated as true or false. 
                            Some examples of conditionals are if statements and switch statements. 
                            Loops are used to execute a section of code a certain number of times while a condition is true. 
                            Some examples of different types of loops include while loops, do while loops, for loops, for of loops, and for in loops.  
                        </p>
                        <p>
                            Object-oriented programming is a model of programming that organizes software around objects. Objects may contain both data and functions. 
                            In object-oriented programming, the goal is to have data and functions that interact with that data be closely linked together.
                            This helps ensure that no other parts of the code can access the data except the functions that are meant to interact with the data. 
                            In object-oriented programming, there are classes that represent a set of properties and methods that are shared by all objects within that class 
                            or objects that are of this type. A class can be thought of as a blueprint for creating an object.
                        </p>
                        <p>
                            Functional programming is a type of programming that focuses on using functions to build programs. In JavaScript functions are 
                            first-class values. Functions can be assigned to variables. Also, functions can receive other functions as arguments. Furthermore, functions 
                            can return functions. A function that receives another function is called a higher-order function. 
                        </p>
                    </article>
                </>
            )
        }
        
export default TopicsPage;