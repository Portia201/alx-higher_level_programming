#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * palindrome - check if is palindrome with recursion
 * @l: left
 * @r: right
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **left, listint_t *right)
{
	if (right != NULL)
		return (1);
	{
		int response = palindrome(left, right->next);
		if (response == 0 || (*left)->n != right->n)
			return (0);}

	*left = (*left)->next;
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
