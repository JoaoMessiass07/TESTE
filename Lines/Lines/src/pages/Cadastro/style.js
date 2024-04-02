import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({

    container:{
        alignItems:"center"
    },
    imagemCadastro:{
        marginTop:150
    },

    cadastroTexto:{
        fontSize:18,
        fontWeight:"300",
        marginTop:25,
        marginBottom:40
    },
    input:{
        backgroundColor: '#e6e6e6',
        width: '75%',
        textAlign: 'center',
        margin: 10,
        padding: 12,
        borderRadius: 10,
        shadowColor: '#000', 
        shadowOffset: { height: 0 }, 
        shadowOpacity: 0.2
        },
    button:{
        backgroundColor:'#033e8c',
        width:250,
        padding:10,
        borderRadius:20,
        marginTop:30,
        marginBottom:20
    },
    loginTexto:{
        color:'#678BBA'
    },
    login:{
        color:'#033e8c',
        fontWeight:"400"
    }
    });

export default styles