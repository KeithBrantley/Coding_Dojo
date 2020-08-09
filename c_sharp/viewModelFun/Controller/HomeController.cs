using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using viewModelFun.Models;

namespace viewModelFun.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            string[] names = new string[]
            {
                "Sally", "Billy", "Joey", "Moose"
            };
            return View(names);
        }

        [HttpGet("numbers")]
        public ViewResult Numbers()
        {
            string[] numbers = new string[]
            {
                "1", "2", "3", "10", "43", "5"
            };
            return View(numbers);
        }

        [HttpGet("users")]
        public ViewResult Users()
        {
            User someUser = new User()
            {
                FirstName = "Sally",
                LastName = "Sanderson"
            };
            User anotherUser = new User()
            {
                FirstName = "Moose",
                LastName = "Philips"
            };
            List<User> viewModel = new List<User>()
            {
                someUser, anotherUser
            };
            return View(viewModel);
        }

        [HttpGet("user")]
        public IActionResult user()
        {
            User somePerson = new User()
            {
                FirstName = "Moose",
                LastName = "Philips"
            };
            return View(somePerson);
        }
    }
}
