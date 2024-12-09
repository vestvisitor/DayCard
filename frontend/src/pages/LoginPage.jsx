import React from 'react';
import { Layout, Menu, theme } from 'antd';

import LoginComponent from "../components/LoginComponent"

const {Content, Footer } = Layout;

const LoginPage = () => {

  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout
      style={{
        minHeight: '100vh',
      }}
    >
                  
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
            background: '#070c3d',
            padding: 12,
            borderRadius: 25
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
          <LoginComponent />
        </div>
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
export default LoginPage;