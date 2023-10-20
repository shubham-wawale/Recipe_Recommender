# Changes compared to Previous Version V2

The team worked on multiple aspects of project revolving around a new feature, a completely new and easy to utilize user interface, database.

---

<p align="center">
  <a href="#functionality">Functionality</a>
  ::
  <a href="#database">Database</a>
  ::
  <a href="#documentation">Documentation</a>
  ::
  <a href="#user-interface">User Interface</a>
</p>

---

## Functionality

Version 2 of project, provided functionalities like filtering the recipees using filters like ingredients, cuisine where multiple ingredients can be used for filters.

The team worked following features to improve upon the previous work.

1. **Adding New Recipes:** Previous version of project didnot support any feature to add new recipes, this needed to be done via command line directly to database. Newer version of the project provides a feature to users to add recipes to the database in a given format.
2. **Updating Ingredient List:** New recipees added contains certain ingredients which are not originally in ingredients table. Therefore, whenever a new recipe is added to database the ingredients table is also updated with the ingredients.
3. **Regex Supported Search for Ingredients:** In addition to using ingredients to filter out recipes, website also supports Type Ahead Drop Down search for ingredients based on the existing recipees ingredients. Provides easy and understandable interface for users to find if recipe with a certain ingredient exists or not. This feature is supported using an ingredients table created.

## Database

Database format was not changed but a new table was added to the database. They are mentioned below.

1. **Ingredients Table:** This version of projects adds various features that requires a set of ingredients used in all the recipees present in database. Instead of filtering those out everytime, team decided to create a new table of these ingredients.

## Documentation

Changes to the documentation were also significant. They are mentioned below.

1. **README:** Team added multiple important points to the documentation. We added instructions about running the project and setting up the database. Various changes that needs to be done before running the project are also mentioned.

## User Interface

The User Interface has been improved from the previous version.

1. **Simple and User Friendly Interface:** Team thought that the previous version of user interface was too colourful and distinguishing various functionality was difficult. Therefore, this version introduces a simple yet user friendly interface with all the functionalities being distinctive.
2. **Add New Recipe Page:** A new page has been added to support adding new recipees features. Users are provided with a button at the top to navigate between two pages.
3. **Card Based Display of Recipees:** A long list of recipees are the result of users search which are shown one after other which requires a lot of scrolling. This causes user to search through complete page before finding a specific recipe. This version changes the format in which recipees are shown. Recipees are shown like a Cards with only important information on it side-by-Side to each other. This provides capacity to shown large number of recipee cards in small space allowing users to find the specific recipe quickly.
4. **Modal View for Recipees:** Card view of recipees shows all the recipees of users search. A specific recipe is shown in Modal View which provides distinct visibility of recipe details from the previous version.
