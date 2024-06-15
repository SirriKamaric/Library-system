from flask import Flask, request, jsonify
import MySQLdb

# Database connection configuration
$DB_HOST = 'localhost'
$DB_USER = 'root'
$DB_PASSWORD = 'toor'
$DB_NAME = 'library'

# Database connection function
function ConnectToDatabase {
    $connectionString = "server='localhost';database='library';uid='root';password='toor'"
    $connection = New-Object MySql.Data.MySqlClient.MySqlConnection($connectionString)
    $connection.Open()
    return $connection
}

# Execute a database query
function ExecuteQuery {
    param(
        [string]$query,
        [object]$params = $null
    )

    $connection = ConnectToDatabase
    $command = $connection.CreateCommand()
    $command.CommandText = $query

    if ($params -ne $null) {
        foreach ($param in $params.GetEnumerator()) {
            $command.Parameters.AddWithValue($param.Name, $param.Value)
        }
    }

    $result = $command.ExecuteReader()
    $data = @()

    while ($result.Read()) {
        $row = @{}
        for ($i = 0; $i -lt $result.FieldCount; $i++) {
            $row[$result.GetName($i)] = $result.GetValue($i)
        }
        $data += $row
    }

    $result.Close()
    $connection.Close()

    return $data
}

# API Key verification function
function RequireApiKey {
    param(
        [System.Management.Automation.ScriptBlock]$ScriptBlock
    )

    return {
        param($context)

        $apiKey = $context.Request.Headers."X-API-Key"
        if ($apiKey -eq '12345') {
            & $ScriptBlock.Invoke($context)
        } else {
            $context.Response.StatusCode = 401
            $context.Response.ContentType = "application/json"
            $context.Response.Write((ConvertTo-Json @{'message' = 'Invalid API key'}))
        }
    }
}

# API Endpoints
function Login {
    param(
        $context
    )

    $data = (ConvertFrom-Json ($context.Request.InputStream -as [System.IO.StreamReader]).ReadToEnd())

    $username = $data.username
    $password = $data.password

    $query = "SELECT * FROM users WHERE user_name = @username AND user_password = @password"
    $result = ExecuteQuery -query $query -params @{username = $username; password = $password}

    if ($result.Count -gt 0) {
        $context.Response.StatusCode = 200
        $context.Response.ContentType = "application/json"
        $context.Response.Write((ConvertTo-Json @{'message' = 'Login successful'}))
    } else {
        $context.Response.StatusCode = 401
        $context.Response.ContentType = "application/json"
        $context.Response.Write((ConvertTo-Json @{'message' = 'Invalid credentials'}))
    }
}

function ManageBooks {
    param(
        $context
    )

    if ($context.Request.HttpMethod -eq 'GET') {
        $query = "SELECT * FROM book"
        $books = ExecuteQuery -query $query

        $context.Response.StatusCode = 200
        $context.Response.ContentType = "application/json"
        $context.Response.Write((ConvertTo-Json @{'books' = $books}))
    } elseif ($context.Request.HttpMethod -eq 'POST') {
        $data = (ConvertFrom-Json ($context.Request.InputStream -as [System.IO.StreamReader]).ReadToEnd())

        $book_title = $data.book_title

        $query = "INSERT INTO book (book_title) VALUES (@book_title)"
        ExecuteQuery -query $query -params @{book_title = $book_title}

        $context.Response.StatusCode = 201
        $context.Response.ContentType = "application/json"
        $context.Response.Write((ConvertTo-Json @{'message' = 'Book added successfully'}))
    }
}

function DeleteBook {
    param(
        $context
    )

    $book_id = $context.Request.Url.Segments[-1]

    $query = "DELETE FROM book WHERE book_id = @book_id"
    ExecuteQuery -query $query -params @{book_id = $book_id}

    $context.Response.StatusCode = 200
    $context.Response.ContentType = "application/json"
    $context.Response.Write((ConvertTo-Json @{'message' = 'Book removed successfully'}))
}

function ManageClients {
    param(
        $context
    )

    if ($context.Request.HttpMethod -eq 'GET') {
        $query = "SELECT * FROM client"
        $clients = ExecuteQuery -query $query

        $context.Response.StatusCode = 200
        $context.Response.ContentType = "application/json"
        $context.Response.Write((ConvertTo-Json @{'clients' = $I apologize, but it seems that the code snippet exceeds the character limit for this response. Could you please provide me with a specific part of the code that you would like assistance with?