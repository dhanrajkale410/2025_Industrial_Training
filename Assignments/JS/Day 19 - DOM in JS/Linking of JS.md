# Linking JavaScript File
- Linking a JavaScript file to an HTML document creates a connection that enables the execution of JavaScript code within the webpage. 
- This is commonly achieved using the script tag in the HTML file, where the src attribute specifies the path to the external JavaScript file. 
- Approximately 90% of modern websites use JavaScript to enhance interactivity and functionality, making this linking process a fundamental part of web development.

## 4 Ways of Linking JS 

> Script Tag inside head tag
- In this example, a Script Tag is placed in the head section of an HTML page.


        <!DOCTYPE html>
        <html>
                <head>
                        <script src = "js_in_head"></script>
                </head>
                <body>
                
                </body>
        </html>

> Script Tag inside Body Tag
- In this example, a Script tag is placed in the body section of an HTML page.

        <!DOCTYPE html>
        <html>
                <head>
                        
                </head>
                <body>
                        <script src = "js_in_body"></script>
                </body>
        </html>

> Script Tag with async attribute
- Asynchronous blocks the parsing of the page.	
- Asynchronous scripts don’t wait for each other. 
- The execution of scripts begins by pause parsing.

        <!DOCTYPE html>
        <html>
                <head>
                        <script src = "js_using_async" async></script>
                </head>
                <body>
                
                </body>
        </html>


> Script Tag with defer attribute
- Deferred never blocks the page.
- Deferred scripts maintain their relative order which means the first script will be loaded first while all others below it will have to wait.
- However, the execution of scripts begins only after parsing is completely finished but before the document’s DOMContentLoadedevent.

        <!DOCTYPE html>
        <html>
                <head>
                        <script src = "js_using_defer" defer></script>
                </head>
                <body>
                
                </body>
        </html>
