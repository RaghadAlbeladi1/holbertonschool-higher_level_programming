#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog subclass of Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal"""

    def sound(self):
        return "Meow"
