# Yarning Circles

Boolean Bears

> [!NOTE]
> This repo has been shared with your group. Use it to develop your group project.
>
> Your group will have received two identical repos - one for your project's back-end, and another for the front-end. Although they are identical right now they are about to diverge, because you'll be using one to create a DRF project and the other to create a React project!

> [!IMPORTANT]  
> Use this `README.md` file to document your MVP using Markdown. Feel free to duplicate the product description aspects between the front-end README and the back-end README, but consider splitting out the technical design aspects to the specific repo that implements them.
>
> An example MVP spec (containing both front- and back-end descriptions) is set out below - you should replace it with your own content! (Remember to delete any "admonition" blocks like this `IMPORTANT` section, the `CAUTION` and `NOTE` sections, etc.)

> [!CAUTION]  
> In order to set up your project, **one** member of the group should clone this repo down, initialise a new React/DRF project, commit, and push.
>
> If more than one group member performs the setup, you'll have Git problems. Check out [the Git collaboration content](https://github.com/SheCodesAus/PlusLessonContent?tab=readme-ov-file#26---group-project) for more on how to use Git as a team.

## Table of Contents

- [Yarning Circles](#yarning-circles)
  - [Table of Contents](#table-of-contents)
  - [Mission Statement](#mission-statement)
  - [Features](#features)
    - [Summary](#summary)
    - [Users](#users)
    - [Courses](#courses)
    - [Collections](#collections)
    - [Pages/Endpoint Functionality](#pagesendpoint-functionality)
    - [Nice To Haves](#nice-to-haves)
  - [Technical Implementation](#technical-implementation)
    - [Back-End](#back-end)
    - [Front-End](#front-end)
    - [Git \& Deployment](#git--deployment)
  - [Target Audience](#target-audience)
  - [Back-end Implementation](#back-end-implementation)
    - [API Specification](#api-specification)
    - [Object Definitions](#object-definitions)
      - [Users](#users-1)
      - [Sticky Notes](#sticky-notes)
    - [Database Schema](#database-schema)
  - [Front-end Implementation](#front-end-implementation)
    - [Wireframes](#wireframes)
      - [Home Page](#home-page)
      - [Collection List Page](#collection-list-page)
    - [Logo](#logo)
    - [Colours](#colours)
      - [Primary](#primary)
      - [Secondary](#secondary)
    - [Font](#font)

## Mission Statement

This project aims to create a dynamic and accessible peer-learning platform that empowers individuals to build knowledge, develop new skills, and learn collaboratively in a supportive environment. The goal is to make learning more accessible by enabling users to create, and participate in shared content. Users will be able to contribute written content across a range of predefined categories, helping others discover content that aligns with their learning preferences.

By combining user-generated material, the platform promotes ongoing skill development and continuous learning. Whether someone is seeking to upskill, explore a new hobby, or connect with others on a shared topic, this platform provides a central space to collaborate, learn, and grow together. The focus on accessibility ensures that users of all experience levels can easily navigate and contribute to their learning communities.

## Features

### Summary

Visitors to the site may browse user created courses on a range of subjects. Creating an account allows users to create courses, enroll in available courses and provide feedback to other users through a course rating system. They may also track their course creation contributions and enrollments via their personal profile page.

Visitor users (not logged in) may;

- Browse courses available.

Account holder (logged in) may;

- Access the full course details
  - Enroll in a course
- Create their own course
  - Course creation allows written content supported by additional uploaded images, videos or pdf documents
- View their own profile
  - Displaying the courses they have created
  - Follow the courses they have enrolled in
  - See badges reflecting their contribution to the site

### Users

| Type           | Access                                                                                                                                                                                                                                                                                                            | Role type assignment                |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| Account holder | <br> - Can log in <br> - Can log out <br> - View course cards <br> - View course details and enroll in courses <br> - Post comments to courses <br> - "Like" and rate courses <br> - Create and manage courses (update and delete) <br> - View sumamry of course creations and course likes via Profile Page page | Educators, learners                 |
| Guest          | <br> - View course cards                                                                                                                                                                                                                                                                                          | Public, anyone visiting the website |

### Courses

| Feature                                        | Access                                                                                                                                                                                                         | Notes/Conditions                                                                                             |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| Create                                         | Can be created by anyone with URL                                                                                                                                                                              | <br> - Limit length of sticky note text <br> - option to add hashtag (TBC: as main text or additional field) |
| Post                                           | Post as Guest                                                                                                                                                                                                  | <br> - Submits Sticky note to Live event board                                                               |
| View                                           | Guests, Approvers and Admin can view posts via Live event board Admin and Approvers can view once status updated from Live                                                                                     |                                                                                                              |
| Edit                                           | Can be edited by Admin and Approvers                                                                                                                                                                           | <br> - Edit sticky note text, eg: for spelling errors before Status is set to approved                       |
| Statuses: Live, Unapproved, Approved, Archived | <br> - Auto status of notes will be ‘live’ based on linked event <br> - Auto status of notes will be unapproved based on closure of linked event <br> - Update to Approved and Archived by Admin and Approvers |                                                                                                              |
| Export                                         | <br> - Export as Admin only                                                                                                                                                                                    | <br> - CSV file <br> - Format: collection, event, sticky note text                                           |
| Flag- Is Exported                              | <br> - Auto flag based on whether Admin has exported the sticky note                                                                                                                                           | <br> - Boolean                                                                                               |
| Link to Collection                             | <br> - Controlled by Admin                                                                                                                                                                                     | <br> - Based on type of event, eg: shecodes flash, plus, other event types.                                  |
| Link to Event                                  | <br> - Auto link based on event URL <br> - Link to event can be edited by Admin                                                                                                                                |                                                                                                              |
| Link to Approver                               | <br> - Controlled by Admin and Approver who creates the event                                                                                                                                                  | <br> - Approver is User who is managing or associated with admin of the event                                |

### Collections

| Feature                           | Access                     | Notes/Conditions           |
| :-------------------------------- | :------------------------- | :------------------------- |
| Assign events to a collection     | <br> - Based on event type |                            |
| Assign approver to a collection   | <br> - admin               |                            |
| Default event board live duration | <br> - Admin               | <br> - Based on event type |
| View event boards by collection   | <br> - Admin, Approver     |                            |
| Export notes by Collection        | <br> - Admin               |                            |

### Pages/Endpoint Functionality

| Endpoint              | functionality                                                                                                                                                                  | comments                                                                                       |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| Create and post notes | <br> - Available to anyone with URL <br> - Add sticky notes <br> - Post sticky notes                                                                                           | <br> - Sticky note ‘feel’ is preferred <br> - Easy to read and accessible <br> - Good contrast |
| Event board           | <br> - Once note is posted, redirect to live session notes <br> - Able to post more notes (redirect back or add directly?) <br> - Live session ends at midnight – day of event | <br> - view live notes <br> - search notes by text/hashtag                                     |
| Admin page            | All admin functions <br> - can also create another admin account                                                                                                               | <br> - Requires auth <br> - initial admin created by DB                                        |
| Register as Approver  | <br> - users can register as approvers <br> - once registered, approver can log in                                                                                             | Requires shecodes email address to be used                                                     |
| Approver page         | Approver functions                                                                                                                                                             | Requires auth Easy to read, accessible, easy to use for new users                              |
| Profile page          | <br> - All registered users <br> - Can view their personal info <br> - Can update their info                                                                                   | Requires auth                                                                                  |

### Nice To Haves

- Register during or after event; Sign up for additional events: Email address, Name, Event
- History of my own notes as Registered user
- Events I have registered for as Registered user
- Be able to edit my own notes – as Registered user but only until its been approved
- Bulk update sticky note status
- QR code generation
- Use QR codes to access event as guest

## Technical Implementation

> [!NOTE]  
> What languages and frameworks will you be using? What kind of database will you be using? How will you deploy the website? Example Below.

### Back-End

- Django / DRF API
- Python

### Front-End

- React / JavaScript
- HTML/CSS

### Git & Deployment

- Heroku
- Netlify
- GitHub

This application's back-end will be deployed to Heroku. The front-end will be deployed separately to Netlify.

We will also use Insomnia to ensure API endpoints are working smoothly (we will utilise a local and deployed environment in Insomnia).

## Target Audience

> [!NOTE]  
> Who is the website for? (approx 100 words). Example below.

This website has two major target audiences: She Codes ‘Leand ‘She Coders’ joining the one-day/short-term workshops.

**She Codes Leaders, Volunteers and Mentors** (administrators) will use this website to assign one-day workshop coders to specific events and/or collections where they can fill-out a “sticky note” win and paste it on the WinsWall. The administrators will then be able to sort, authorise and delete these stickies and easily download the data in a CSV file. This website is targeted towards this group in order to automate a normally menial task.

**She Coders** (laypeople) will use this website to post their Win on a WinWall board, keep track of what events they’ve attended and also view previously written wins. This website is targeted to this group in order to prevent loss of paper data (physical sticky notes) and also make the WinsWall more interactive.

## Back-end Implementation

### API Specification

| HTTP Method | URL                                 | Purpose                                                                                                                                  | Request Body                                                                                                      | Successful Response Code | Authentication and Authorization                      |
| :---------- | :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----------------------- | :---------------------------------------------------- |
| POST        | /login                              | Allow users to log in                                                                                                                    | ““Username”:”string”, “password”:”string”                                                                         | 200                      | Token auth                                            |
| POST        | /logout                             | Allow users to log out ( end active session)                                                                                             | ““Username”:”string”, “password”:”string”                                                                         | 200                      | Will clear user log in session \- remove stored token |
| POST        | /Register                           | Create new student or approver user                                                                                                      | “Username”:”string”, “FullName”: “string” “Email”:”string”,”Password”:”string”, ”Password2”:”string”,             | 201                      | Admin                                                 |
| PUT         | /Profile/ID                         | Edit user                                                                                                                                | “Username”:”string”, “FullName”: “string” “Email”:”string”, “Avatar”:”string”, “Bio”:”string”, “Socials”:”string” | 200                      | Admin, approver or student with matching ID           |
| GET         | /Profile/ID                         | View User profile                                                                                                                        | NA                                                                                                                | 200                      | Any                                                   |
| DELETE      | /User/ID                            | Delete user                                                                                                                              | NA                                                                                                                | 204                      | Admin, approver or student with matching ID           |
| POST        | /EventCollection                    | Create new Event Collection                                                                                                              | “Title”:”string”, “IsExported”:”boolean” “Approver”: integer                                                      | 201                      | Admin                                                 |
| PUT         | /EventCollection/Id                 | Update Event collection                                                                                                                  | “Title”:”string”, “IsExported”:”boolean”                                                                          | 200                      | Admin, Approver linked to event?                      |
| DELETE      | /EventCollection/Id                 | Delete Event collection                                                                                                                  | NA                                                                                                                | 204                      | Admin                                                 |
| POST        | /EventBoard/                        | Create new Event board                                                                                                                   | “Title”: “string”, “StartDate”:”datetime”, “EndDate:”datetime”                                                    | 201                      | Admin, approvers                                      |
| PUT         | /EventBoard/ID                      | Update Event board                                                                                                                       | “Title”: “string”, “StartDate”:”datetime”, “EndDate:”datetime”                                                    | 200                      | Admin, approvers                                      |
| DELETE      | /EventBoard/ID                      | Delete Event board                                                                                                                       | NA                                                                                                                | 204                      | Admin or author of event                              |
| GET         | /EventBoard/ID                      | Get Event board details                                                                                                                  | NA                                                                                                                | 200                      | Open access                                           |
| POST        | /stickyNote/                        | Create a new sticky note as Guest user                                                                                                   | “WinComment”:”string”                                                                                             | 201                      | Open access                                           |
| GET         | /stickyNotes/?Status=Live\&Event.ID | Get Sticky notes for an event Use query params to filter by event ID and Status                                                          | NA                                                                                                                | 200                      | Open access                                           |
| GET         | /stickyNotes/?Event.ID              | Get Sticky notes for an event                                                                                                            | NA                                                                                                                | 200                      | Admin, approvers                                      |
| GET         | /stickyNotes/                       | Export sticky notes as CSV (eg:response.setContentType("text/csv")) Can optionally filter by: event ID, Status, isexported, collectionId | NA                                                                                                                | 200                      | Admin                                                 |
| PUT         | /stickyNotes/ID                     | Edit sticky note, update status of sticky note to Approved or Archived                                                                   | “WinComment”:”string”                                                                                             | 200                      | Admin, approvers                                      |
| POST        | /StickyStatus                       | Create available statuses for stickyNotes                                                                                                | “StatusName”:”string”                                                                                             | 201                      | Admin                                                 |
| GET         | /StickyStatus                       | Get all statuses                                                                                                                         | NA                                                                                                                | 200                      | Admin                                                 |

### Object Definitions

> [!NOTE]  
> Define the actual objects that your API returns. The example GET method above says it returns “all projects”, so we need to define what a “project” looks like. Example below.

#### Users

| Field             | Data type |
| :---------------- | :-------- |
| _User_ID (PK)_    |           |
| _Username_        | string    |
| FullName          | string    |
| _Email_           | string    |
| _Password_        | string    |
| _Password2_       | string    |
| Auth_ID (FK)      | integer   |
| StickyNoteId (FK) | integer   |
| Event_Id (FK)     | integer   |
| Collection_Id(FK) | integer   |
| Avatar            | string    |
| Bio               | string    |
| SocialLink        | string    |

#### Sticky Notes

| Field                 | Data Type |
| :-------------------- | :-------- |
| Sticky_ID (PK)        | integer   |
| WinComment            | string    |
| Guest                 | boolean   |
| UserId (FK)           | integer   |
| Event_Id (FK)         | integrer  |
| Collection_Id (FK)    | integrer  |
| Sticky_Status_ID (FK) | integrer  |

> [!NOTE]  
> ... etc

### Database Schema

> [!NOTE]  
> Insert an image of your database schema (could be a photo of a hand-drawn schema or a screenshot of a schema created using a tool such as ​​https://drawsql.app/). Example below.

![Our database schema](./img/schema.png)

## Front-end Implementation

### Wireframes

> [!NOTE]  
> Insert image(s) of your wireframes (could be a photo of hand-drawn wireframes or a screenshot of wireframes created using a tool such as https://www.mockflow.com/).

See all wireframes and how Admins, Approvers and Students would see the Win Wall website: https://www.figma.com/file/cvP0Kc7lAX39Fvo12C5aLa/Win-Wall?node-id=22%3A1345

#### Home Page

![](./img/homepage.png)

#### Collection List Page

![](./img/listpage.png)

> [!NOTE]  
> etc...

### Logo

![](./img/logo.png)

### Colours

#### Primary

![](./img/primary.png)

#### Secondary

![](./img/secondary.png)

### Font

(We will create a ‘highlight-text’ font style in CSS with the glow effect as per the above - to use on hero section)
Raleway
Google fonts:

```css
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;700&display=swap");
font-family: "Raleway", sans-serif;
```

(When Raleway is not available the standard font to be used is the Calibri font family)

![](./img/fonts.png)
