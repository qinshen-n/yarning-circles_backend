# Yarning Circles
> Boolean Bears

## Table of Contents

- [Yarning Circles](#yarning-circles)
  - [Table of Contents](#table-of-contents)
  - [Mission Statement](#mission-statement)
  - [Features](#features)
    - [Summary](#summary)
    - [Users](#users)
    - [Courses](#courses)
    - [Courses](#courses-1)
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
      - [Courses](#courses-2)
      - [Comment](#comment)
      - [Likes](#likes)
      - [Rating](#rating)
    - [Database Schema](#database-schema)


## Mission Statement

This project aims to create a dynamic and accessible peer-learning platform that empowers individuals to build knowledge, develop new skills, and learn collaboratively in a supportive environment. The goal is to make learning more accessible by enabling users to create, and participate in shared content. Users will be able to contribute written content and additional uploaded learning material across a range of predefined categories, helping others discover content that aligns with their learning preferences.

By combining user-generated material, the platform promotes ongoing skill development and continuous learning. Whether someone is seeking to upskill, explore a new hobby, or connect with others on a shared topic, this platform provides a central space to collaborate, learn, and grow together. The focus on accessibility ensures that users of all experience levels can easily navigate and contribute to their learning communities.
By combining user-generated material, the platform promotes ongoing skill development and continuous learning. Whether someone is seeking to upskill, explore a new hobby, or connect with others on a shared topic, this platform provides a central space to collaborate, learn, and grow together. The focus on accessibility ensures that users of all experience levels can easily navigate and contribute to their learning communities.

## Features

### Summary 
Visitors to the site may browse user created courses on a range of subjects. Creating an account allows users to create courses, enroll in available courses and provide feedback to other users through a course rating system. They may also track their course creation contributions and enrollments via their personal profile page.

### Users

| Type               | Access                                                                                                                                                                                                                                                                                             | Role type assignment                                |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| Account holder           | - Can log in  <br> - Can log out  <br> - View course cards  <br> - View course details and enroll in courses  <br> - Post comments to courses  <br> - "Like" and rate courses  <br> - Create and manage courses (update and delete)  <br> - View sumamry of course creations and course likes via Profile Page page                                                                                                                                                              | Educators, learners            |
| Guest              | - View course cards                                                                                                                                 | Public, anyone visiting the website |

### Courses
### Courses

| Feature                                        | Access                                                                                                                                                                                                           | Notes/Conditions                                                                                              |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| Create                                         | Logged in user        | - Organised by specified categories <br> - Allows written content supported by additional uploaded images, videos or pdf documents  |
| Post                                           | Logged in user        | Submits course to website                                                                |
| View                                           | - Public may view all all course cards on Home Page <br> - Logged in user may access full course details    | - Trying to access full course without login, will navigate to login page    |
| Edit                                           | Courses can be edited by the course creator        | - Update button only visible on course page to creator <br> - All course fields are editable        |
| Delete                                         | Courses can be deleted by the course creator (logged in)     | - Delete button only visible on course page to creator <br> - Course deletion confirmation required via popup message      |
| Max students                                   | Public and logged in users can view via course card     | - Course willm not allow further enrollments if max student cap is reached      |
| Open/Closed                                    | Public and logged in users can view via course card  |   - Open allows more enrollments until max student cap, then courses closes and is not visible on Home Page. <br> - Already enrolled students may then access the course via their Profile Page.             |


### Pages/Endpoint Functionality

| Endpoint              | functionality                                                                                                                                                                     | comments                                                                                         |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Landing Page          | - All users  <br> - Displays introductory information regarding the website                                                                                    |                                                                                     |
| Home Page | - All users   <br> - View existing, open courses via course card   <br> - View featured courses (most liked) <br> - Search and/or sort course list                | <br> -   <br> -   <br> -  |
| About Page           | - Features short bio of development team  <br> - links to team member social media | <br> -                                       |
| Create Account Page            | - All users                                                                                                                  | - only 1 type of user                                         |
| Login Page  | - Users can log in using created username and password                                                                                               |                                                        |
| Create Course Page         | - Create course <br> - Written content entered into course content field, which supports formatting <br> Supported by additional uploaded images, videos or pdf documents                                                                                                                                                                | - Only these fields are necessary; <b> -                                |
| Course Page          | - Logged in, enrolled users may view  <br> - Can "like" page  <br> - Can leave comment <br> - Can rate course <br> Can view all course content and open supporting material  <br> Course owner will see update and delete buttons                                                                                  | Requires auth    
| Update Course Page   | - Logged in, owner users may view  <br> - Can update all course fields                                                                                  | Requires auth  |
| Profile Page          | - Can view their personal info, date joined, courses created, courses liked <br> - show badges earned through contributing to course creation                                                                                | Requires auth                                                                                    |

### Nice To Haves

- Moderation - Superuser or admin user who can delete any courses, comments.
- Moderation - Admin approval of courses after submission but before going live on website
- User Experience - Profile picture upload
- User Experience - Course picture upload
- Moderation/User Experience - Report to admin button

## Technical Implementation

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

The platform is designed for digital users of all abilities, with a strong emphasis on inclusivity and accessibility. It supports adult learners who are looking for flexible, self-paced opportunities to engage with content across a variety of topics. The platform aims to provide an environment where anyone can confidently participate, gain new skills, and connect through shared interests. A platform where users are enabled to share their knowledge with others by creating and sharing course content on categories they are interested in and have the information.

## Back-end Implementation

### API Specification

| HTTP Method | URL                                 | Purpose                                                                                                                                  | Request Body                                                                                                       | Successful Response Code | Authentication and Authorization                      |
| :---------- | :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :----------------------- | :---------------------------------------------------- |
| POST        | /login                              | Allow users to log in                                                                                                                    | ““Username”:”string”, “password”:”string”                                                                          | 200                      | Token auth                                            |
| POST        | /logout                             | Allow users to log out ( end active session)                                                                                             | ““Username”:”string”, “password”:”string”                                                                          | 200                      | Will clear user log in session \- remove stored token |
| POST        | /createaccount                           | Create new student or approver user                                                                                                      | “Username”:”string”, “Email”:”string”, ”Password”:”string”              | 201                      | Public                                                 |
| GET         | /users/:id                         | View User profile                                                                                                                        | NA                                                                                                                 | 200                      | Logged in user                                                   |
| POST        | /createcourse                    | Create new course                                                                                                              | "title": "", "brief_description": "", "course_content": "", "category": "", "image": null, "is_open": true, "max_students": null, "difficulty_level": "", "duration_in_hours": null, "learning_objectives": "", "enrollment_end": null, "status": "published"                                                    | 201                      | Logged in user                                                 |
| GET        | /course/:id                 | View course details and content                                                                                                                  |                                                                            | 200                      | Logged in user                      |
| PUT         | /course/update/:id                 | Update course details                                                                                                                  |                                                                            | 200                      | Logged in owner of course                      |
| DELETE      | /course/:id                 | Delete course                                                                                                                  | NA                                                                                                                 | 204                      | Logged in owner of course                                                 |
| GET        | courses/:id/comments/           | Get all comments for specfic course                                                                                                                  |                                                      | 200                      |                                       |
| POST        | courses/:id/comments/           | Post comment on course page                                                                                                                   | "content": "", "rating": null, "course": null                                                     | 201                      | Logged in user                                      |
| GET        | courses/:id/likes/           | Get all likes for specific course                                                                                                                  | “Title”: “string”, “StartDate”:”datetime”, “EndDate:”datetime”                                                     | 200                      |                                       |
| POST        | courses/:id/likes/           | Post like on course page                                                                                                                   | "course": null                                                     | 201                      | Logged in user                                      |
| GET         | courses/features/                      | Get featured courses (most liked courses)                                                                                                                  | NA                                                                                                                 | 200                      | Public                                           |
| GET         | courses/:id/ratings/ | Get ratings for specific course                                                          | NA                                                                                                                 | 200                      | Public                                           |
| POST        | courses/:id/ratings/                        | Rate a course (out of 5 stars)                                                                                                   |   "course": null, "score": null                                                                                            | 201                      | Logged in user                                           |
| POST        | courses/image-url/                        | Create URL to view uploaded AWS hosted images                                                                                                   |                                                                                               | 201                      | Logged in user                                           |

### Object Definitions

> [!NOTE]  
> Define the actual objects that your API returns. The example GET method above says it returns “all projects”, so we need to define what a “project” looks like. Example below.

#### Users
| Field              | Data type |
| :----------------- | :-------- |
| *User\_ID (PK)*    |           |
| *Username*         | string    |
| *Email*            | string    |
| *Password*         | string    |
| Auth\_ID (FK)      | integer   |
| date_joined        | datetime  |

#### Courses
| Field                   | Data Type |
| :---------------------------- | :-------- |
| Courses\_ID (PK)         | integer   |
| title              | string    |
| brief_description                   | text   |
| course_content             | text   |
| category          | string  |
| owner (FK)     | integer  |
| created_at | datetime  |
| updated_at | datetime  |
| image | URL field  |
| is_open | boolean  |
| max_students | integer  |
| difficulty_level | string  |
| duration_in_hours | integer  |
| learning_objectives | text  |
| enrollment_end | datetime  |
| views_count | integer  |
| completion | integer  |
| status | string  |
| rating_count | integer  |
| rating_average | integer  |

#### Comment
| Field                   | Data Type |
| :---------------------------- | :-------- |
| ID (PK)         | integer   |
| content              | string    |
| course (FK)  | string  |
| author  (FK)                 | string   |
| created_at | datetime  |

#### Likes
| Field                   | Data Type |
| :---------------------------- | :-------- |
| ID (PK)         | integer   |
| course (FK)  | string |
| author (FK)                   | string   |
| created_at | datetime  |
| unique_together | string, string |

#### Rating
| Field                   | Data Type |
| :---------------------------- | :-------- |
| ID (PK)         | integer   |
| course (FK) | string  |
| user (FK)            | string   |
| score                | integer   |
| created_at | datetime  |
| updated_at | datetime  |


> [!NOTE]  
> ... etc

### Database Schema

![Our database schema](./database.drawio.svg)  

