import React, { useEffect, useState } from 'react';
import { Layout, Card, Button } from 'antd';
// import logo from '../public/images/logo.png';
import axios from 'axios';
import Cookies from 'js-cookie';

const { Meta } = Card;

const CardComponent = (props) => {

  const IMG = (imgName) => {
    return `/@fs/home/michael/PycharmProjects/DayCard/static/${imgName}`
  }

  const GenerateWish = () => {
    axios.get('http://127.0.0.1:5000/cards/make',
      {
        withCredentials: true,
        headers: {
          'accept': 'application/json',
          "Authorization": `Bearer ${Cookies.get('access_token_cookie')}`
          }}
      ).then(r => {
        console.log(r.data)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

    return (
        
        <Layout>
            <Card
                hoverable
                style={{
                    width: 540
                }}
                cover={
                  <img src={IMG(props.props.image)} />
                }
        >
          <Meta 
            style={{
              textAlign: 'center'
            }}
            title="Quote of th day:" 
            description={`${props.props.text}\r${props.props.author}`} 
          />
        </Card>
            <Button 
                style={{
                    padding: 30,
                    margin: 10
                }}
                type="primary" 
                onClick={GenerateWish}
            >
                Magic!
            </Button>
        </Layout>
        
    );
};
export default CardComponent;
