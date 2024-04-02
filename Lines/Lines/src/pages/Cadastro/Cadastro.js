import React, { useState } from "react";
import { View, Text, TextInput, Alert, Image} from 'react-native';
import styles from "../Cadastro/style";
import iconeUsuario from '../../img/iconeUsuario.png';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../../Componentes/Firebase/Firebase';
import { Button } from "react-native-elements";


export default function Cadastro({ navigation }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    async function createUser() {
      
      try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const successMessage = 'Cadastro criado com sucesso! ' + userCredential.user.email;
        Alert.alert('Sucesso', successMessage);
      } catch (error) {
        const errorMessage = 'Erro ao criar a conta. Verifique o campo de e-mail e senha.';
        Alert.alert('Erro', errorMessage);

      }
    }

    return (
        <View style={styles.container}>
          <View style={styles.imagemCadastro} ><Image source={iconeUsuario} style={{width:200, height:200}}></Image></View>
            <Text style={styles.cadastroTexto}>Informe seu email e crie uma senha!</Text>

            <TextInput 
              placeholder="Informe seu e-mail"
              placeholderTextColor='#6d6d6d'
              value={email}
              onChangeText={value => setEmail(value)}
              style={styles.input}
            />

            <TextInput 
              placeholder="Crie uma senha com 6 dígitos"
              placeholderTextColor='#6d6d6d'
              value={password}
              onChangeText={value => setPassword(value)}
              style={styles.input}
              maxLength={6}
              secureTextEntry={true}
            />

            <Button
              buttonStyle={styles.button} 
              title="Cadastrar"
              onPress={() => createUser()}
            />

              < Text
              style={styles.loginTexto}
              onPress={() => navigation.navigate('Login')}>
                Fez o cadastro? Faça aqui seu
             <Text style={styles.login}> Login</Text>!
            </Text> 
            
        </View>
    )
}