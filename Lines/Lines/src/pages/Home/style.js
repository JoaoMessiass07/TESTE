import { StyleSheet } from "react-native";

const style = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent:"center"
    },
    iconeAlerta:{
        width:48, 
        height:48,
        position: "absolute",
        bottom: 75,
        right: 13,
        zIndex: 999
    }

})

export default style;