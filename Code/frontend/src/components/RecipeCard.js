import React from "react";
import { Box, SimpleGrid, Card, CardHeader, Heading, Text, CardBody, CardFooter, Button, Image } from "@chakra-ui/react"


const RecipeCard = (props) => {
    const handleClick = ()=> {
        props.handler(props.recipe);
    }
    return (
        <>
            <Card _hover={{transform: "scale(1.05)", bg: "green.300", transitionDuration: "4" ,cursor: "pointer"}} onClick={handleClick}>
                <CardHeader>
                    <Heading size='md'>{props.recipe.TranslatedRecipeName}</Heading>
                </CardHeader>
                <CardBody>
                    <Text>Cooking Time: {props.recipe.TotalTimeInMins} mins</Text>
                    <Text>Rating: {props.recipe['Recipe-rating']}</Text>
                    <Text>Diet Type: {props.recipe['Diet-type']}</Text>
                </CardBody>
                <Image
                    objectFit='cover'
                    src={props.recipe["image-url"]}
                    width={"90%"}
                    height={"40%"}
                    m={"auto"}
                    mb="2"
                />
            </Card>
        </>
    )
}

export default RecipeCard;