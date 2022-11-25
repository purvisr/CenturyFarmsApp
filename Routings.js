import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Wrapper from './reactComponents/Wrapper'
import FarmPage from "./reactComponents/FarmsMap";

const Stack = createNativeStackNavigator();

// Used for navigating to a specific farm's page
const Routings = () => (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Wrapper"
          component={Wrapper}
          options={{headerShown: false}}
        />
        <Stack.Screen name="FarmPage" component={FarmPage} options={{title: ""}} />
      </Stack.Navigator>
    </NavigationContainer>
)

export default Routings;