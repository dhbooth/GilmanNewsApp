//
//  Article Ideas.m
//  The Gilman News 5.0
//
//  Created by Davis Booth on 8/25/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import "Article Ideas.h"

@interface Article_Ideas ()

@end

@implementation Article_Ideas

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

- (void)callToWeb{
    NSError *error;
    NSString *getWebInfo = @"http://www.gilmannewsapp.squarespace.com/xcode-test";
    NSURL *webUnformatted = [NSURL URLWithString:getWebInfo];
    NSString *webFormatted = [NSString stringWithContentsOfURL:webUnformatted encoding:NSASCIIStringEncoding error:&error];
    label.text = webFormatted;
}


- (IBAction)button:(id)sender {
    MFMailComposeViewController *mailController = [[MFMailComposeViewController alloc] init];
    mailController.mailComposeDelegate = self;
    
    [mailController setToRecipients:@[@"thegilmannews@gmail.com"]];
    [mailController setSubject: [email.text stringByAppendingString: @" Article Idea Proposition"]];
    [mailController setMessageBody:idea.text isHTML:NO];
    [self presentViewController:mailController animated:YES completion:nil];
}

- (IBAction)touch:(id)sender {
    [self.view endEditing:YES];
}

- (void)mailComposeController:(MFMailComposeViewController *)controller didFinishWithResult:(MFMailComposeResult)result error:(NSError *)error
{
    [self dismissViewControllerAnimated:YES completion:nil];
    
}

- (BOOL) textFieldShouldReturn:(UITextField *)textField
{
    [email resignFirstResponder];
    [idea resignFirstResponder];
    return YES;
}

@end
