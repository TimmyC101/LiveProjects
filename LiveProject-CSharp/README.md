# Live-Projects

## Overview
C# Live Project - These live projects took place within the ASP.NET web framework and utilized the MVC design pattern.  

My main tasks during the first 2-week sprint involved creating a dynamic password validation box and improving overall mobile compatibility for the various pages of the site.  While working on these two tasks, I developed and evolved my understanding of CSS and JS.  Specifically, I gained a deep understanding of flexboxes and how they can be leveraged to create adaptable websites that can be compatible with many devices and screen widths without needing excessive code.  Additionally, I learned how to use JavaScript to create powerful, reactive modules within the website.

During the second 2-week sprint, I spent most of my time learning about animations, JQuery, SVG, and how to utilize them together to create dynamic navigation bars and navbar icons. I created many pilot projects to design hamburger icons that both animate on various mouseevents or follow the mouse horizontally or vertically.  I also created multiple navigation bars, both horizontal and vertical, to appear/dissapear or translate on/off the screen based on various click or mouseover events.  I even wrote custom code to slide the body content with the expanding navigation bar, rather than simply overlapping it.  Lastly, I created a footer with text that perpetually translated left to right upon hover, and reset upon mouse exit.


## Creating Dynamic Password Validation Box
To be completely honest, most of this code was recycled so I won't take credit for it or paste it below; however, this task did help me understand how to utilize JavaScript to add and remove classes from website content, based on constantly changing conditions, in order to create dynamic, responsive websites. Essentially, every keyup within the password input box triggers a series of if statements, which then check for various conditions and add/remove classes depending upon those conditions.  The classes added/removed have varying CSS stylings, and the result of the CSS/JS working together is a dynamic password validation box.


## Improve Mobile Compatibility Across Entire Project
This task was a lot more involved.  I spent multiple days researching flexboxes, various CSS stylings, and numerous JS functions in order to determine the best way to create a mobile friendly application.  Initially, the code you see below was organized into html tables, which from my understanding, are not ideal for creating mobile applications.  Essentially, I converted everything to either:
a) a series of flex columns within a single, wrappable flex row, or
b) a series of flex rows within a single flex column
This, combined with some CSS styling and JS, resulted in incredibly adaptable web pages.
Additionally, I wrote a JavaScript function that identified mobile users based on screen size and dynamically resized the table columns in order to prevent "word scruntch" (technical term).

# Sample HTML
    <div class="IndexBody">
        <div class="text-center">
            <h2>Company News</h2>
            <p>@Html.ActionLink("Create New", "Create")</p>
        </div>
        <div class="news-table">
            <div class="news-row text-info font-weight-bold">
                <div class="news-title">
                    @Html.DisplayNameFor(model => model.Title)
                </div>
                <div class="news-item">
                    @Html.DisplayNameFor(model => model.NewsItem)
                </div>
                <div class="news-expire">
                    @Html.DisplayNameFor(model => model.ExpirationDate)
                </div>
                <div class="news-modify">
                    <p>Modify Item</p>
                </div>
            </div>

            @foreach (var item in Model) {
                <div class="news-row">
                    <div class="news-title">
                        @Html.DisplayFor(modelItem => item.Title)
                    </div>
                    <div class="news-item">
                        @Html.DisplayFor(modelItem => item.NewsItem)
                    </div>
                    <div class="news-expire">
                        @Convert.ToDateTime(item.ExpirationDate).ToString("MM-dd-yyyy")
                    </div>
                    <div class="news-modify">
                        @Html.ActionLink("Edit", "Edit", new { id = item.NewsId }) |
                        @Html.ActionLink("Details", "Details", new { id = item.NewsId }) |
                        @Html.ActionLink("Delete", "Delete", new { id = item.NewsId })
                    </div>
                </div>
            }
        </div>
    </div>

# Sample CSS
    /* Begin styling for mobile compatibility - News page */

    .news-table {
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .news-row {
        display: flex;
    }

    .news-title {
        display: flex;
        flex: 1 1 20%;
        padding: 5px;
        /*min-width: 6rem;*/
    }

    .news-item {
        display: flex;
        flex: 2 1 40%;
        padding: 5px;
    }

    .news-expire {
        display: flex;
        flex: 1 1 18%;
        padding: 5px 5px 5px 20px;
        min-width: 4.5rem;
    }

    .news-modify {
        display: flex;
        flex: 1 1 22%;
        height: 25%;
        flex-wrap: wrap;
        padding: 5px;
    }

    @media (max-width: 575.98px) {
        .news-modify { /* Remove modification buttons on narrow screen */
            display: none;
            position: absolute;
        }
        .news-expire {
            padding: 5px;
        }
    }

    /* End styling for mobile compatibility - News page */

# Sample JS
    // Set column width of "news-title" class div 
    // based on widest text for mobile users (prevents misaligned columns)
    // Applies to News/Index
    $(document).ready(function () {
        if (window.location.pathname == '/CompanyNews') { // Only run on this page to prevent execution elsewhere
            var targetWidth = 575.98; // Align with smallest @media from Bootstrap.css
            if ($(window).width() <= targetWidth) {
                var ele = document.getElementsByClassName("news-title");
                var max = 0;
                for (i = 0; i < ele.length; i++) { //iterate thru each class element to find widest
                    if (ele[i].clientWidth > max) {
                        max = ele[i].clientWidth;
                    }
                }
                $(".news-title").css('min-width', max+"px"); //add css styling to all ".news-title" class elements
            }
        }
    });

## Styled & Animated Footer
I added background styling to the footer with fading opacity, and then wrote JavaScript to animate the text.  When the user hovers over the footer, the text begins moving left to right until it is hidden, then resets back to the left side offscreen, and begins sliding to the right again.  When the mouse leaves the footer, the text resets to the middle of the footer element.

#HTML
    <footer>
        <div class="slider">
            &copy; @DateTime.Now.Year - Management Portal
        </div>
    </footer>

#CSS
    footer {
        display: flex;
        width: 250px;
        margin: 10px auto;
        padding: 10px;
        align-items: center;
        justify-content: center;
        background: rgb(255,255,255);
        background: radial-gradient(circle, rgba(255,255,255,0.4) 25%, rgba(195,195,195,0.2) 50%, rgba(140,140,160,0) 100%);
        border: 1px solid rgba(0, 0, 0, 0.325);
        border-radius: 0.25rem;
        overflow: hidden;
    }

#JS
    $(document).ready(function () {

        var x = 0;
        var stoploop = undefined;

        $("footer").on("mouseenter", slide);
        $("footer").on("mouseleave", stopslide);

        function slide() {
            if (!stoploop) {
                x += 2;
                $(".slider").css("transform", "translateX(" + x + "px");
                if (x > 250) {
                    x = -250;
                }
                window.requestAnimationFrame(slide);
            }
        };

        function stopslide() {
            stoploop = true
            x = 0;
            $(".slider").css("transform", "translateX(" + x + "px");
            window.setTimeout(function () {
                stoploop = false;
            }, 50);
        };

    });

##Animated Navbar and Navbar Icons
I made nearly a dozen pilot projects while experimenting with various effects, and obviously will not include all of the code here.  I will just demonstrate a menu icon that translates with the mouse. Hovering over the icon expands the navigation bar and slides the menu icon to the right.  The html is not included because I did not write the majority of it.

#Pictures



#CSS
    .sidenav {
        height: 100%;
        width: 230px;
        float: left;
        background-color: none;
        overflow-x: hidden;
        position: fixed;
        z-index: 1;
    }

    .navbar-toggler {
        padding-left: 15px;
        position: absolute;
        transition: transform 700ms cubic-bezier(0.2, 1, 0.2, 1);
        cursor: default;
        z-index: 2;
        pointer-events: none; 
        /* Because an invisible div box is left behind on the left side of the navbar, we need to be able to click through this */
    }

    /* Hamburger styling and translation for hover */

    .animated-icon {
        width: 36px;
        height: 29px;
        position: relative;
        margin: 0px;
        cursor: default;
        background-color: white;
        pointer-events: all; /* Added since we turned off pointer events on the parent */
        transform: translateX(0px);
        transition: all 1s cubic-bezier(0.2, 1, 0.2, 1);
    }

    .animated-icon.open {
        transform: translateX(170px);
    }

    .animated-icon span {
        display: block;
        position: absolute;
        height: 3px;
        width: 30px;
        opacity: 1;
        left: 3px;
        background: #595959;
    }

    .animated-icon span:nth-child(1) {
        top: 5px;
    }

    .animated-icon span:nth-child(2), .animated-icon span:nth-child(3) {
        top: 13px;
    }

    .animated-icon span:nth-child(4) {
        top: 21px;
    }

    /* Hamburger border styling */

    .icon-bg {
        position: absolute;
        width: 55px;
        height: 37px;
        z-index: -1;
        margin: -4px;
        margin-left: -15px;
    }



#JS
    // Slide navbar icon with mouse cursor
    $(document).ready(function () {
        $(window).on("mousemove", function (e) {
            var yPos = e.pageY - 140;
            if (e.pageY > 140) { // Prevents icon from going into header
                $(".icon-slider").css("transform", "translateY(" + yPos + "px");
            }
            else {
                $(".icon-slider").css("transform", "translateY(" + 0 + "px");
            }
        });
    });

    // toggle navbar and icon translation via mouseover
    $(document).ready(function () {
        $(".animated-icon, .animated-icon.span").on("mouseenter", function () {
            $(".navbar-collapse").addClass("show");
            $(".animated-icon").addClass("open");
        });
        $("#navigation").on("mouseleave", function () {
            $(".navbar-collapse").removeClass("show");
            $(".animated-icon").removeClass("open");
        });
    });