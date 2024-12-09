import React from 'react';
import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Form, Input} from 'antd';
import Image from '../public/images/logo.png';
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";

const LoginForm = () => {

  const navigate = useNavigate();

  const loginRequest = (data) => {
    axios.post('http://127.0.0.1:5000/users/login',
      data = data,
      {
        headers: {
          'accept': 'application/json',
          // 'X-CSRF-TOKEN': Cookies.get('csrf_access_token'),
        }
      }
      ).then(r => {

      Cookies.set('access_token_cookie', r.data.access_token_cookie)
      navigate('/');
      
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const onFinish = (values) => {
    loginRequest(values)
  };

  return (
    
    <Form
      style={{
        textAlign: "center",
        padding: '0 48px'
      }}
      name="login"
      initialValues={{
        remember: true,
      }}
      onFinish={onFinish}
    >
      
      <a href='/'>
      <img 
        src={Image}
        width={125}
        height={125}
      ></img>
      </a>

      <h1>Login</h1>
      <Form.Item
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your Username!',
          },
        ]}
      >
        <Input prefix={<UserOutlined />} placeholder="Username" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your Password!',
          },
        ]}
      >
        <Input prefix={<LockOutlined />} type="password" placeholder="Password" />
      </Form.Item>

      <Form.Item>
        <Button block type="primary" htmlType="submit">
          Log in
        </Button>
        or <a href="/#signup">Register now!</a>
      </Form.Item>
    </Form>
  );
};
export default LoginForm;