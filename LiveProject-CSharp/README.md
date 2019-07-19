# Live-Projects

## Overview
C# Live Project - This live project took place within the ASP.NET web framework and utilized the MVC design pattern.  My main tasks during this 2-week period involved creating a dynamic password validation box and improving overall mobile compatibility for the various pages of the site.  While working on these two tasks, I developed and evolved my understanding of CSS and JS.  Specifically, I gained a deep understanding of flexboxes and how they can be leveraged to create adaptable websites that can be compatible with many devices and screen widths without needing excessive code.  Additionally, I learned how to use JavaScript to create powerful, reactive modules within the website.


## Creating Dynamic Password Validation Box
To be completely honest, most of this code was recycled so I won't take credit for it or paste it below; however, this task did help me understand how to utilize JavaScript to add and remove classes from website content, based on constantly changing conditions, in order to create dynamic, responsive websites. Essentially, every keyup within the password input box triggers a series of if statements, which then check for various conditions and add/remove classes depending upon those conditions.  The classes added/removed have varying CSS stylings, and the result of the CSS/JS working together is a dynamic password validation box.

    ADD PICTURE OF PASSWORD VALIDATION BOX


## Improve Mobile Compatibility Across Entire Project
This task was a lot mroe involved.  I spent multiple days researching flexboxes, various CSS stylings, and numerous JS functions in order to determine the best way to create a mobile friendly application.  Initially, the code you see below was organized into html tables, which from my understanding, are not ideal for creating mobile applications.  Essentially, I converted everything to either:
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