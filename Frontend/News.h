//
//  News.h
//  The Gilman News 5.0
//
//  Created by Davis Booth on 8/25/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface News : UIViewController
{
    
    IBOutlet UIWebView *webView;
    
}
- (IBAction)backButton:(id)sender;

- (IBAction)subscribe:(id)sender;

@end
