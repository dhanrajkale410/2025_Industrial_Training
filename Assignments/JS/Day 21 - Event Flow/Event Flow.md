# Event Flow

- Event flow in JavaScript describes how events propagate through the Document Object Model (DOM) when an event is triggered.

- There are Three Key Points :

## 1. Event Bubbling (Event Propagation)

- Definition: When an event occurs on an element, it bubbles up from the target element to its ancestors (parent → grandparent → up to the document).

- It is the default behavior in the DOM.

- Handlers attached to parent elements can catch events triggered on child elements.

        <div id="parent">
        <button id="child">Click Me</button>
        </div>

        <script>
        document.getElementById("child").addEventListener("click", () => {
            console.log("Child Clicked");
        });

        document.getElementById("parent").addEventListener("click", () => {
            console.log("Parent Clicked - Bubbling");
        });
        </script>

        Output when Button Clicked :
        Child Clicked
        Parent Clicked - Bubbling

## 2. Event Capturing (Trickling Phase)

- Definition: The event starts at the top of the DOM tree (like document) and trickles down to the target element.

- Not used by default.

- You must set the third parameter of addEventListener to true.

        document.getElementById("parent").addEventListener("click",() => {
            console.log("Parent - Capturing");
        },
        true // capturing enabled
        );

        Order of logs when button is clicked with both bubbling & capturing:
        Parent - Capturing
        Child Clicked
        Parent Clicked - Bubbling


## 3. Event Delegation

- Definition: A technique where you attach a single event listener to a parent element instead of adding multiple listeners to individual child elements.

- Efficient for dynamically added elements.

- Works due to event bubbling.

        <ul id="list">
        <li>Item 1</li>
        <li>Item 2</li>
        </ul>

        <script>
        document.getElementById("list").addEventListener("click", (e) => {
            if (e.target.tagName === "LI") {
            console.log("Clicked:", e.target.textContent);
            }
        });
        </script>

# Summary

| Concept          | Direction          | Key Use                             |
| ---------------- | ------------------ | ----------------------------------- |
| Event Bubbling   | Target → Document  | Default event flow                  |
| Event Capturing  | Document → Target  | Optional, rarely used directly      |
| Event Delegation | Relies on bubbling | Handle many child events via parent |


