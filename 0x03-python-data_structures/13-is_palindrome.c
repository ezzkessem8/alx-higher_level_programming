#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer pointing to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int arr[2048];  /* Assuming the max size of the list is 2048 */
    int i = 0, j;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        arr[i] = current->n;
        current = current->next;
        i++;
    }

    i--;
    for (j = 0; j <= i / 2; j++, i--)
    {
        if (arr[i] != arr[j])
            return (0);
    }

    return (1);
}

