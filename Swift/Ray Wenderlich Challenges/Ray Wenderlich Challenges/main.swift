//
//  main.swift
//  Ray Wenderlich Challenges
//
//  Created by ChrisHome on 23/06/2015.
//  Copyright (c) 2015 ChristmasHouse. All rights reserved.
//
// Solutions to the challenges in http://www.raywenderlich.com/76349/swift-ninja-part-1

import Foundation

// Challenge 1 - Swap two values in one line
func swap<T>(inout a: T, inout with b:T)
{
    (a, b) = (b, a)
}


// Challenge 2
func flexStrings(s0: String = "none", s1: String = "") -> String
{
    return s0 + s1
}


// Challenge 3
func sumAny(anys: Any...) -> String {
    return String((anys.map({item in
        switch item {
        case "" as String, 0 as Int:
            return -10
        case let s as String where s.toInt() > 0:
            return s.toInt()!
        case is Int:
            return item as! Int
        default:
            return 0
        }
    }) as [Int]).reduce(0) {
        $0 + $1
        })
}
