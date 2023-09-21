// Q01_valid_palindrome.cpp

// Tershire
// 2023 SEP 21


#include <iostream>
#include <string>

// prototype
bool fB(const std::string& s);


// main ///////////////////////////////////////////////////////////////////////
int main(int argc, char **argv)
{
    std::string s;
    s = "A man, a plan, a canal: Panama";
    s = "a";
    s = "";
    s = "race a car";
    
    std::cout << fB(s) << std::endl;

    return 0;
}

// function ///////////////////////////////////////////////////////////////////
// ----------------------------------------------------------------------------
// two-pointer
// 4 ~ 8 [ms]
bool fB(const std::string& s)
{
    const int LENGTH = s.size();

    int i_L = 0;
    int i_R = LENGTH - 1;

    for (;;)
    {
        // std::cout << i_L << " " << i_R << std::endl;

        // skip non-alphanumerics (left)
        while (!isalnum(s[i_L]))
        {
            i_L += 1;

            // case: all non-alphanumerics
            if (i_L >= LENGTH - 1)
                return true;
        }

        // skip non-alphanumerics (right)
        while (!isalnum(s[i_R]))
        {
            i_R -= 1;
        }

        // termination
        if (i_L >= i_R)
            break;

        // compare
        if (tolower(s[i_L]) != tolower(s[i_R]))
            return false;

        // update
        i_L += 1;
        i_R -= 1;
    }

    return true;
}
