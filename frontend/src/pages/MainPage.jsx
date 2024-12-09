import { React, useEffect, useState } from 'react';
import { Layout, Menu, theme } from 'antd';
import {
  HomeOutlined,
  LoginOutlined,
  LogoutOutlined,
  UserOutlined
} from '@ant-design/icons';
import axios from 'axios';
import Cookies from 'js-cookie';
import CardComponent from '../components/CardComponent.jsx'
import Card from 'antd/es/card/Card.js';

const { Header, Content, Footer } = Layout;

function getItem(label, key, icon, click) {
  return {
    key,
    icon,
    label,
    onClick: click
  };
}


const MainPage = () => {

  const [magicData, setMagicData] = useState([]);

  const GetCard = () => {
    axios.get('http://127.0.0.1:5000/cards/read',
      {
        withCredentials: true,
        headers: {
          'accept': 'application/json',
          "Authorization": `Bearer ${Cookies.get('access_token_cookie')}`
          }}
      ).then(r => {
        console.log(r.data)
        setMagicData(r.data)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const [items, setItems] = useState([]);

  const Authenticate = () => {
    axios.get('http://127.0.0.1:5000/users/me',
      {
        withCredentials: true,
        headers: {
          'accept': 'application/json',
          "Authorization": `Bearer ${Cookies.get('access_token_cookie')}`
          }}
      ).then(r => {
        
        setItems(
          [
            getItem('My DayCard', '1', <UserOutlined />),
            getItem('Logout', '3', <LogoutOutlined />, logOut),
          ]
        );

        GetCard();
      
    })
    .catch(function (error) {
      setItems(
        [
          getItem(<a href='/'>Home</a>, '1', <HomeOutlined />),
          getItem(<a href='/#login'>Login</a>, '2', <LoginOutlined />),
        ]
    );
      console.log(error);
    });
  }

  useEffect(() => {
    Authenticate();
  }, []);

  function logOut() {
    axios.post('http://127.0.0.1:5000/users/logout',
      ).then(r => {
        Cookies.remove('access_token_cookie');
        window.location.reload();
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout
      style={{
        minHeight: '100vh',
      }}
    >
      <Header
        style={{
          position: 'sticky',
          top: 0,
          zIndex: 1,
          width: '100%',
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <div className="demo-logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['1']}
          expandIcon={<img src={Image} width={25} height={25}/>}
          items={items}
          style={{
            flex: 1,
            minWidth: 0,
          }}
        >
        </Menu>
      </Header>
            
      <Content
        style={{
          padding: '0 48px',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <div
          style={{
            alignContent: 'center',
            margin: '16px 0',
            padding: 24,
            minHeight: 360,
            background: colorBgContainer,
            borderRadius: borderRadiusLG,
          }}

        >
          <CardComponent 
            props={magicData} 
          />
          
        </div>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        Ant Design ©{new Date().getFullYear()} Created by Ant UED
      </Footer>
    </Layout>
  );
};
export default MainPage;