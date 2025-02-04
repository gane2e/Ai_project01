package com.example.backend.controller;

import com.example.backend.entity.User;
import com.example.backend.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.annotation.RequestScope;

import java.util.List;

@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
@CrossOrigin(origins = "http://localhost:8081")
public class UserController {

    private final UserRepository userRepository;

    @GetMapping(value = "/register")
    public User register(@RequestBody User user) {
        return userRepository.save(user);
    }

    @GetMapping("/read")
    public List<User> getUsers() {
        return userRepository.findAll();
    }

}
