//  
import Form from "./components/Form.js";
import Header from "./components/Header";
import recipeDB from "./apis/recipeDB";
import RecipeList from "./components/RecipeList";
import AddRecipe from "./components/AddRecipe.js";
import React, { Component } from "react";
import { Tabs, Tab, TabList,TabPanel, TabPanels, Box } from "@chakra-ui/react";
import RecipeLoading from "./components/RecipeLoading.js";
import Nav from "./components/Navbar.js";

// Main component of the project
class App extends Component {
  // constructor for the App Component
  constructor() {
    super();

    this.state = {
      cuisine: "",
      //NoIngredients : 0,
      ingredients: new Set(),
      recipeList: [],
      email: "",
      flag: false,
      isLoading: false
    };
  }

  // Function to get the user input from the Form component on Submit action
  handleSubmit = async (formDict) => {
    this.setState({
      isLoading: true
    })
    console.log(formDict)
    this.setState({
      // cuisine: cuisineInput,
      //NoIngredients: noIngredientsInput,
      ingredients: formDict["ingredient"],
      cuisine: formDict["cuisine"],
      email: formDict["email_id"],
      flag: formDict["flag"],
    });

    const mail = formDict["email_id"];
    const flag = formDict["flag"];
    const items = Array.from(formDict["ingredient"]);
    const cuis = formDict["cuisine"];
    this.getRecipeDetails(items, cuis, mail, flag);
    //  alert(typeof(ingredientsInput["cuisine"]));
  };

  getRecipeDetails = async (ingredient, cuis, mail, flag) => {
    try {
      const response = await recipeDB.get("/recipes", {
        params: {
          CleanedIngredients: ingredient,
          Cuisine: cuis,
          Email: mail,
          Flag: flag,
        },
      });
      this.setState({
        recipeList: response.data.recipes,
        isLoading: false
      });
    } catch (err) {
      console.log(err);
    }
  };

  render() {
    return (
      <div>
        <Nav />

        {/* handleSubmit function is being sent as a prop to the form component*/}
        <Tabs variant='soft-rounded' colorScheme='green'>
          <TabList ml={10}>
            <Tab>Search Recipe</Tab>
            <Tab>Add Recipe</Tab>
          </TabList>
          <TabPanels>
            <TabPanel>
            <Box display="flex">
            <Form sendFormData={this.handleSubmit} />
            {this.state.isLoading ? <RecipeLoading/> : <RecipeList recipes={this.state.recipeList} /> }
            </Box>
            </TabPanel>
            <TabPanel>
              <AddRecipe />
            </TabPanel>
          </TabPanels>
        </Tabs>

        {/* RecipeList is the component where results are displayed.
        App's recipeList state item is being sent as a prop
        */}

      </div>
    );
  }
}

export default App;
